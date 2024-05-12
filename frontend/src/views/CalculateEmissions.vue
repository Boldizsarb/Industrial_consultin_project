<template>
  <navbar />
  <div class="min-h-screen flex justify-center items-center">
    <div
      class="w-full h-full p-32 flex flex-col lg:flex-row shadow-lg rounded-lg bg-gray-500 bg-opacity-50 p-4 transition-opacity duration-700 ease-in"
      :class="{ 'opacity-100': isAnimated }"
    >
      <!-- Map Section -->
      <div class="w-full lg:w-1/2 mt-4 lg:mt-0">
        <div id="map" class="w-full h-96 lg:h-full"></div>
      </div>
      <!-- Form and Results Section with Vertical Scrollable Content and Max Height -->
      <div
        class="w-full m-8 lg:w-1/2 space-y-4 lg:overflow-y-auto scrollbar-thin scrollbar-thumb-gray-500 scrollbar-track-gray-200"
      >
        <h1 class="text-3xl font-bold text-white mb-2">Calculate Emissions</h1>
        <div>
          <Co2TreesBar :co2Emission="co2Emission" />
        </div>
        <p class="text-lg text-white mb-4">
          Here you will be able to see various information regarding your
          emission history.
        </p>
        <div class="flex justify-between items-start space-x-4 mb-4">
          <div class="flex flex-col w-1/2 space-y-2">
            <input
              v-if="this.travelMode === `DRIVING`"
              id="reg-input"
              type="text"
              placeholder="Enter your Reg"
              class="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
              v-if="this.travelMode === `DRIVING`"
              id="people-input"
              type="number"
              placeholder="How many people"
              class="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
              id="origin-input"
              type="text"
              placeholder="Enter origin"
              class="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <input
              id="destination-input"
              type="text"
              placeholder="Enter destination"
              class="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>
          <div class="flex-shrink-0 w-1/2">
            <div class="bg-gray-100 p-4 rounded-lg shadow">
              <ul class="list-disc list-inside space-y-2">
                <label class="flex items-center cursor-pointer">
                  <input
                    type="radio"
                    name="travelMode"
                    value="DRIVING"
                    v-model="travelMode"
                    class="form-radio h-4 w-4 text-blue-600 mr-2"
                  />
                  <span class="text-sm font-medium text-gray-700">Driving</span>
                </label>

                <label class="flex items-center cursor-pointer">
                  <input
                    type="radio"
                    name="travelMode"
                    value="WALKING"
                    v-model="travelMode"
                    class="form-radio h-4 w-4 text-green-600 mr-2"
                  />
                  <span class="text-sm font-medium text-gray-700">Walking</span>
                </label>

                <label class="flex items-center cursor-pointer">
                  <input
                    type="radio"
                    name="travelMode"
                    value="BICYCLING"
                    v-model="travelMode"
                    class="form-radio h-4 w-4 text-yellow-500 mr-2"
                  />
                  <span class="text-sm font-medium text-gray-700"
                    >Bicycling</span
                  >
                </label>

                <label class="flex items-center cursor-pointer">
                  <input
                    type="radio"
                    name="travelMode"
                    value="TRANSIT"
                    v-model="travelMode"
                    class="form-radio h-4 w-4 text-purple-600 mr-2"
                  />
                  <span class="text-sm font-medium text-gray-700">Transit</span>
                </label>
              </ul>
            </div>
          </div>
        </div>
        <div
          class="flex flex-col sm:flex-row items-center justify-center space-y-2 sm:space-y-0 sm:space-x-2"
        >
          <button
            @click="searchRoute"
            class="w-1/2 py-2 px-4 bg-slate-800 text-white rounded hover:bg-blue-700 focus:outline-none focus:bg-blue-700"
          >
            Search Route
          </button>
          <button
            @click="addRoute"
            class="w-1/2 py-2 px-4 bg-slate-800 text-white rounded hover:bg-blue-700 focus:outline-none focus:bg-blue-700"
          >
            Add Route
          </button>
        </div>
        <div
          class="flex flex-col bg-white shadow-lg rounded-lg overflow-hidden w-full bg-gray-200 bg-opacity-50 p-4 transition-opacity duration-700 ease-in"
        >
          <p class="text-lg text-slate-700 mb-4 w-full text-center">Results</p>

          <div
            v-for="(route, index) in routeAlternatives"
            :key="index"
            @click="selectRoute(index)"
            :class="[
              'cursor-pointer p-2 my-1 rounded-md transition-colors duration-300 ease-in-out shadow-sm',
              index === selectedRouteIndex.value
                ? 'bg-blue-500 text-white'
                : 'hover:bg-blue-500 hover:text-white',
            ]"
          >
            <p class="text-sm font-semibold">Route {{ index + 1 }}:</p>
            <p class="text-xs">Summary: {{ route.summary }}</p>
            <p class="text-xs">Distance: {{ route.distance }}</p>
            <p class="text-xs">Duration: {{ route.duration }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <myFooter />
</template>

<script>
/* global google */
import { onMounted, ref, watch } from "vue";
import navbar from "@/components/NavBar.vue";
import myFooter from "@/components/Footer.vue";
import Co2TreesBar from "@/components/Co2TreesBar.vue";

export default {
  name: "LocationSearch",
  components: {
    navbar,
    myFooter,
    Co2TreesBar,
  },
  data() {
    return {
      isAnimated: false,
    };
  },
  setup() {
    let co2Emission = ref(200);
    const map = ref(null);
    const travelMode = ref("DRIVING");
    const directionsService = new google.maps.DirectionsService();
    const routeAlternatives = ref([]);
    const selectedRouteDetails = ref({});
    const lastResponse = ref(null);
    const directionsDisplayers = ref([]);
    const selectedRouteIndex = ref(null);

    onMounted(() => {
      const mapOptions = {
        center: { lat: 50.909698, lng: -1.404351 },
        zoom: 10,
        mapTypeControl: false,
        streetViewControl: false,
        fullscreenControl: false,
      };

      map.value = new google.maps.Map(
        document.getElementById("map"),
        mapOptions,
      );

      // Set up autocomplete inputs
      new google.maps.places.Autocomplete(
        document.getElementById("origin-input"),
      );
      new google.maps.places.Autocomplete(
        document.getElementById("destination-input"),
      );

      // Adjust zoom level when route alternatives are available
      watch(routeAlternatives, () => {
        if (routeAlternatives.value.length > 0) {
          const bounds = new google.maps.LatLngBounds();
          routeAlternatives.value.forEach((route) => {
            if (route.legs) {
              route.legs.forEach((leg) => {
                if (leg.steps) {
                  leg.steps.forEach((step) => {
                    bounds.extend(step.start_location);
                    bounds.extend(step.end_location);
                  });
                }
              });
            }
          });
          map.value.fitBounds(bounds);
        }
      });
    });

    const searchRoute = () => {
      const origin = document.getElementById("origin-input").value;
      const destination = document.getElementById("destination-input").value;
      let people = 1;
      let reg = "";
      if (!origin.trim()) {
        alert("Origin field cannot be empty.");
        return;
      }
      if (!destination.trim()) {
        alert("Destination field cannot be empty.");
        return;
      }
      if (travelMode.value === "DRIVING") {
        people = document.getElementById("people-input").value;
        reg = document.getElementById("reg-input").value;
        if (!reg.trim()) {
          alert("Reg field cannot be empty.");
          return;
        }
        if (people === 0 || !people) {
          people = 1;
        }
      }
      directionsService.route(
        {
          origin: origin,
          destination: destination,
          travelMode: google.maps.TravelMode[travelMode.value],
          provideRouteAlternatives: true,
        },
        (response, status) => {
          if (status === "OK") {
            lastResponse.value = response; // Store the response for later use

            // Clear existing routes from the map before setting new ones
            directionsDisplayers.value.forEach((displayer) =>
              displayer.setMap(null),
            );
            directionsDisplayers.value.length = 0;

            response.routes.forEach((_, index) => {
              const directionsRenderer = new google.maps.DirectionsRenderer({
                map: map.value,
                directions: response,
                routeIndex: index,
                polylineOptions: {
                  strokeColor: "grey",
                },
              });
              directionsDisplayers.value.push(directionsRenderer); // Store the renderer
            });
            routeAlternatives.value = response.routes.map((route, index) => ({
              index,
              summary: route.summary,
              distance: route.legs[0].distance.text,
              duration: route.legs[0].duration.text,
              people: people,
              reg: reg,
            }));
            selectedRouteIndex.value = 0;
          } else {
            window.alert("Directions request failed due to " + status);
          }
        },
      );
    };
    const selectRoute = (selectedIndex) => {
      selectedRouteIndex.value = selectedIndex;

      // Update the styles of the selected route renderer
      directionsDisplayers.value.forEach((renderer, index) => {
        renderer.setOptions({
          polylineOptions: {
            strokeColor: index === selectedIndex ? "blue" : "grey",
          },
        });
      });

      // Update selected route details for display
      const selectedRoute = routeAlternatives.value[selectedIndex];
      selectedRouteDetails.value = {
        distance: selectedRoute.distance,
        duration: selectedRoute.duration,
      };

      // Start the trip for the selected route
      startTrip(selectedIndex);
    };

    const startTrip = (selectedIndex) => {
      const selectedRoute = lastResponse.value.routes[selectedIndex];
      const startLocation = selectedRoute.legs[0].start_location;
      const endLocation = selectedRoute.legs[0].end_location;
      processTransitDetails(selectedRoute, selectedIndex);
      // Clear existing routes from the map before setting the new one
      directionsDisplayers.value.forEach((displayer) => displayer.setMap(null));
      directionsDisplayers.value = [];
      // Create a new DirectionsRenderer for the selected route
      const directionsRenderer = new google.maps.DirectionsRenderer({
        map: map.value,
        directions: lastResponse.value,
        routeIndex: selectedIndex,
        polylineOptions: {
          strokeColor: "blue",
        },
      });

      directionsDisplayers.value.push(directionsRenderer);

      // Set the map bounds to include the start and end locations
      const bounds = new google.maps.LatLngBounds();
      bounds.extend(startLocation);
      bounds.extend(endLocation);
      map.value.fitBounds(bounds);
    };

    const getCo2Emission = async (selectedIndex, transport, dist) => {
      const selectedRoute = routeAlternatives.value[selectedIndex];
      console.log(selectedRoute);
      let distance = dist;
      let people = selectedRoute.people;
      let reg = selectedRoute.reg;
      const miles = distance * 0.621371;
      let totalCo2Emission = 0;
      console.log("CO2:", co2Emission.value);
      if (transport === "DRIVING") {
        try {
          const response = await fetch("/calculate_emission", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              reg: reg,
              miles: miles,
              num_pessangers: people,
            }),
          });
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const result = await response.json();
          const { total_emmission_in_miles } = result;
          totalCo2Emission += total_emmission_in_miles;
        } catch (error) {
          console.error("Error calculating CO2 emissions:", error);
        }
      } else if (transport === "BUS") {
        try {
          const response = await fetch("/calculate_bus_emission", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              miles: miles,
              num_pessangers: people,
            }),
          });

          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const result = await response.json();
          const { message } = result;
          totalCo2Emission += message;
        } catch (error) {
          console.error("Error calculating CO2 emissions:", error);
        }
      } else if (transport === "TRAIN") {
        try {
          const response = await fetch("/calculate_train_emission", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              miles: miles,
              num_pessangers: people,
            }),
          });
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          // Parse the JSON response
          const result = await response.json();
          const { message } = result;
          totalCo2Emission += message;
        } catch (error) {
          console.error("Error calculating CO2 emissions:", error);
        }
      }
      co2Emission.value = totalCo2Emission;
      console.log("CO2:", co2Emission.value);
    };

    const processTransitDetails = (route, selectedIndex) => {
      // Initialize all distance variables to 0
      let carDist = 0;
      let busDist = 0;
      let trainDist = 0;

      // Iterate through all legs in the route
      route.legs.forEach((leg) => {
        leg.steps.forEach((step) => {
          // Check if the step contains transit details
          if (step.transit) {
            const transitDetails = step.transit;
            const vehicleType = transitDetails.line.vehicle.type;
            let distance = step.distance.value || "Unknown distance";
            // Categorize based on vehicle type
            if (vehicleType === "BUS") {
              busDist += distance;
            } else if (vehicleType === "HEAVY_RAIL") {
              trainDist += distance;
            }
          } else {
            let distance = step.distance.value || "Unknown distance";
            if (step.travel_mode === "DRIVING") {
              carDist += distance;
            }
          }
        });
      });
      if (carDist > 0) {
        getCo2Emission(selectedIndex, "DRIVING", carDist * 0.001);
      } else if (busDist > 0) {
        getCo2Emission(selectedIndex, "BUS", busDist * 0.001);
      } else if (trainDist > 0) {
        getCo2Emission(selectedIndex, "TRAIN", trainDist * 0.001);
      }
    };

    return {
      searchRoute,
      selectRoute,
      travelMode,
      routeAlternatives,
      selectedRouteDetails,
      selectedRouteIndex,
      co2Emission,
    };
  },
  mounted() {
    setTimeout(() => {
      this.isAnimated = true;
    }, 100);
  },
};
</script>
