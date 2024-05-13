<template>
  <div>
    <navbar />

    <div class="relative bg-blueGray-100">
      <section class="bg-white border-b pt-32">
        <div class="px-4 md:px-10 mx-auto w-full">
          <div>
            <h1 class="text-3xl font-bold text-black mb-2">
              Monthly Users Updates
            </h1>
            <div class="flex flex-wrap">
              <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
                <div
                  class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
                >
                  <div class="flex-auto p-4">
                    <div class="flex flex-wrap">
                      <div
                        class="relative w-full pr-4 max-w-full flex-grow flex-1"
                      >
                        <h5
                          class="text-blueGray-400 uppercase font-bold text-xs"
                        >
                          Trips
                        </h5>
                        <span class="font-semibold text-xl text-blueGray-700">
                          {{ this.thisMonthTrips.toFixed(0) }}
                        </span>
                      </div>
                      <div class="relative w-auto pl-4 flex-initial">
                        <div
                          class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full bg-red-500"
                        >
                          <i class="fas fa-route"></i>
                        </div>
                      </div>
                    </div>
                    <div class="text-sm text-blueGray-400 mt-4">
                      <div
                        v-if="
                          this.getPercentage(
                            this.lastMonthTrips,
                            this.thisMonthTrips,
                          ) > 0
                        "
                      >
                        <span class="mr-2 text-red-500">
                          <i class="fas fa-arrow-up"></i>
                          {{
                            Math.abs(
                              this.getPercentage(
                                this.lastMonthTrips,
                                this.thisMonthTrips,
                              ),
                            ).toFixed(2)
                          }}
                          %
                        </span>
                        <span class="whitespace-nowrap">Since last month</span>
                      </div>
                      <div
                        v-else-if="
                          this.getPercentage(
                            this.lastMonthTrips,
                            this.thisMonthTrips,
                          ) <= 0
                        "
                      >
                        <span class="mr-2 text-emerald-500">
                          <i class="fas fa-arrow-down"></i>
                          {{
                            Math.abs(
                              getPercentage(
                                this.lastMonthTrips,
                                this.thisMonthTrips,
                              ),
                            ).toFixed(2)
                          }}
                          %
                        </span>
                        <span class="whitespace-nowrap">Since last month</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
                <div
                  class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
                >
                  <div class="flex-auto p-4">
                    <div class="flex flex-wrap">
                      <div
                        class="relative w-full pr-4 max-w-full flex-grow flex-1"
                      >
                        <h5
                          class="text-blueGray-400 uppercase font-bold text-xs"
                        >
                          CO2 Emissions
                        </h5>
                        <span class="font-semibold text-xl text-blueGray-700">
                          {{ this.thisMonthCo2.toFixed(0) }}
                        </span>
                      </div>
                      <div class="relative w-auto pl-4 flex-initial">
                        <div
                          class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full bg-orange-500"
                        >
                          <i class="fas fa-cloud"></i>
                        </div>
                      </div>
                    </div>
                    <div class="text-sm text-blueGray-400 mt-4">
                      <div
                        v-if="
                          this.getPercentage(
                            this.lastMonthCo2,
                            this.thisMonthCo2,
                          ) < 0
                        "
                      >
                        <span class="mr-2 text-red-500">
                          <i class="fas fa-arrow-up"></i>
                          {{
                            Math.abs(
                              this.getPercentage(
                                this.lastMonthCo2,
                                this.thisMonthCo2,
                              ),
                            ).toFixed(2)
                          }}
                          %
                        </span>
                        <span class="whitespace-nowrap">Since last month</span>
                      </div>
                      <div
                        v-else-if="
                          this.getPercentage(
                            this.lastMonthCo2,
                            this.thisMonthCo2,
                          ) >= 0
                        "
                      >
                        <span class="mr-2 text-emerald-500">
                          <i class="fas fa-arrow-down"></i>
                          {{
                            Math.abs(
                              this.getPercentage(
                                this.lastMonthCo2,
                                this.thisMonthCo2,
                              ),
                            ).toFixed(2)
                          }}
                          %
                        </span>
                        <span class="whitespace-nowrap">Since last month</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
                <div
                  class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
                >
                  <div class="flex-auto p-4">
                    <div class="flex flex-wrap">
                      <div
                        class="relative w-full pr-4 max-w-full flex-grow flex-1"
                      >
                        <h5
                          class="text-blueGray-400 uppercase font-bold text-xs"
                        >
                          Trees saved
                        </h5>
                        <span class="font-semibold text-xl text-blueGray-700">
                          {{ this.thisMonthTrees.toFixed(0) }}
                        </span>
                      </div>
                      <div class="relative w-auto pl-4 flex-initial">
                        <div
                          class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full bg-pink-500"
                        >
                          <i class="fas fa-tree"></i>
                        </div>
                      </div>
                    </div>
                    <div class="text-sm text-blueGray-400 mt-4">
                      <div
                        v-if="
                          this.getPercentage(
                            this.lastMonthTrees,
                            this.thisMonthTrees,
                          ) <= 0
                        "
                      >
                        <span class="mr-2 text-emerald-500">
                          <i class="fas fa-arrow-up"></i>
                          {{
                            Math.abs(
                              this.getPercentage(
                                this.lastMonthTrees,
                                this.thisMonthTrees,
                              ),
                            ).toFixed(2)
                          }}
                          %
                        </span>
                        <span class="whitespace-nowrap">Since last month</span>
                      </div>
                      <div
                        v-else-if="
                          this.getPercentage(
                            this.lastMonthTrees,
                            this.thisMonthTrees,
                          ) > 0
                        "
                      >
                        <span class="mr-2 text-red-500">
                          <i class="fas fa-arrow-down"></i>
                          {{
                            Math.abs(
                              this.getPercentage(
                                this.lastMonthTrees,
                                this.thisMonthTrees,
                              ),
                            ).toFixed(2)
                          }}
                          %
                        </span>
                        <span class="whitespace-nowrap">Since last month</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="w-full lg:w-6/12 xl:w-3/12 px-4">
                <div
                  class="relative flex flex-col min-w-0 break-words bg-white rounded mb-6 xl:mb-0 shadow-lg"
                >
                  <div class="flex-auto p-4">
                    <div class="flex flex-wrap">
                      <div
                        class="relative w-full pr-4 max-w-full flex-grow flex-1"
                      >
                        <h5
                          class="text-blueGray-400 uppercase font-bold text-xs"
                        >
                          0% Co2 Trips
                        </h5>
                        <span class="font-semibold text-xl text-blueGray-700">
                          {{ this.thisMonthZero.toFixed(0) }}</span
                        >
                      </div>
                      <div class="relative w-auto pl-4 flex-initial">
                        <div
                          class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 shadow-lg rounded-full bg-emerald-500"
                        >
                          <i class="fas fa-seedling"></i>
                        </div>
                      </div>
                    </div>
                    <div class="text-sm text-blueGray-400 mt-4">
                      <div
                        v-if="
                          this.getPercentage(
                            this.lastMonthZero,
                            this.thisMonthZero,
                          ) <= 0
                        "
                      >
                        <span class="mr-2 text-emerald-500">
                          <i class="fas fa-arrow-up"></i>
                          {{
                            Math.abs(
                              this.getPercentage(
                                this.lastMonthZero,
                                this.thisMonthZero,
                              ),
                            ).toFixed(2)
                          }}
                          %
                        </span>
                        <span class="whitespace-nowrap">Since last month</span>
                      </div>
                      <div
                        v-else-if="
                          this.getPercentage(
                            this.lastMonthZero,
                            this.thisMonthZero,
                          ) > 0
                        "
                      >
                        <span class="mr-2 text-red-500">
                          <i class="fas fa-arrow-down"></i>
                          {{
                            Math.abs(
                              this.getPercentage(
                                this.lastMonthZero,
                                this.thisMonthZero,
                              ),
                            ).toFixed(2)
                          }}
                          %
                        </span>
                        <span class="whitespace-nowrap">Since last month</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <svg
        class="wave-top"
        viewBox="0 0 1439 147"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
      >
        <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
          <g transform="translate(-1.000000, -14.000000)" fill-rule="nonzero">
            <g class="wave" fill="#f8fafc">
              <path
                d="M1440,84 C1383.555,64.3 1342.555,51.3 1317,45 C1259.5,30.824 1206.707,25.526 1169,22 C1129.711,18.326 1044.426,18.475 980,22 C954.25,23.409 922.25,26.742 884,32 C845.122,37.787 818.455,42.121 804,45 C776.833,50.41 728.136,61.77 713,65 C660.023,76.309 621.544,87.729 584,94 C517.525,105.104 484.525,106.438 429,108 C379.49,106.484 342.823,104.484 319,102 C278.571,97.783 231.737,88.736 205,84 C154.629,75.076 86.296,57.743 0,32 L0,0 L1440,0 L1440,84 Z"
              ></path>
            </g>
            <g transform="translate(1.000000, 15.000000)" fill="#FFFFFF">
              <g
                transform="translate(719.500000, 68.500000) rotate(-180.000000) translate(-719.500000, -68.500000) "
              >
                <path
                  d="M0,0 C90.7283404,0.927527913 147.912752,27.187927 291.910178,59.9119003 C387.908462,81.7278826 543.605069,89.334785 759,82.7326078 C469.336065,156.254352 216.336065,153.6679 0,74.9732496"
                  opacity="0.100000001"
                ></path>
                <path
                  d="M100,104.708498 C277.413333,72.2345949 426.147877,52.5246657 546.203633,45.5787101 C666.259389,38.6327546 810.524845,41.7979068 979,55.0741668 C931.069965,56.122511 810.303266,74.8455141 616.699903,111.243176 C423.096539,147.640838 250.863238,145.462612 100,104.708498 Z"
                  opacity="0.100000001"
                ></path>
                <path
                  d="M1046,51.6521276 C1130.83045,29.328812 1279.08318,17.607883 1439,40.1656806 L1439,120 C1271.17211,77.9435312 1140.17211,55.1609071 1046,51.6521276 Z"
                  opacity="0.200000003"
                ></path>
              </g>
            </g>
          </g>
        </g>
      </svg>

      <section class="px-4 md:px-10 mx-auto w-full -m-24 pb-32">
        <div>
          <div class="flex flex-wrap">
            <div class="w-full xl:w-8/12 mb-12 xl:mb-0 px-4">
              <div class="text-white">
                <h1 class="text-3xl font-bold text-black mb-2">
                  Monthly Carbon Usage
                </h1>
                <BarChart :monthValues="monthValues" />
              </div>
            </div>
            <div class="w-full xl:w-4/12 px-4">
              <div
                class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6 shadow-lg rounded"
              >
                <div class="rounded-t mb-0 px-4 py-3 bg-transparent">
                  <div class="flex flex-wrap items-center">
                    <div class="relative w-full max-w-full flex-grow flex-1">
                      <div class="w-full p-4">
                        <h2 class="text-2xl font-bold text-gray-700 mb-4">
                          Last Trips Details
                        </h2>
                        <table class="table-auto w-full">
                          <thead>
                            <tr class="bg-green-800 text-white">
                              <th class="px-4 py-2">Date</th>
                              <th class="px-4 py-2">Distance</th>
                              <th class="px-4 py-2">CO2 Emitted</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr
                              v-for="(trip, index) in userTrips"
                              :key="index"
                              class="bg-white border-b"
                            >
                              <td class="px-4 py-2">{{ trip.tripDate }}</td>
                              <td class="px-4 py-2">{{ trip.tripDist }}</td>
                              <td class="px-4 py-2">{{ trip.tripCo2 }}</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
  <myFooter />
</template>

<script>
import BarChart from "@/components/LineChart.vue";
import navbar from "@/components/NavBar.vue";
import myFooter from "@/components/Footer.vue";

export default {
  name: "DashBoard",
  components: {
    BarChart,
    navbar,
    myFooter,
  },
  data() {
    return {
      isAnimated: false,
      lastMonthTrips: 0,
      thisMonthTrips: 0,
      lastMonthCo2: 0,
      thisMonthCo2: 0,
      lastMonthTrees: 0,
      thisMonthTrees: 0,
      lastMonthZero: 0,
      thisMonthZero: 0,
      userTrips: [],
      monthValues: {},
    };
  },
  methods: {
    getCookie(name) {
      let cookieArray = document.cookie.split(";");
      for (let i = 0; i < cookieArray.length; i++) {
        let cookiePair = cookieArray[i].split("=");
        if (name === cookiePair[0].trim()) {
          return decodeURIComponent(cookiePair[1]);
        }
      }
      return null;
    },
    getUserCo2Emmissions() {
      const token = this.getCookie("token");
      fetch(`${process.env.VUE_APP_BACKEND_URL}/userTotalEmissions`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token: token,
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          if (data.message) {
            alert(data.message);
          }
          this.monthValues = data.month_values;
        })
        .catch((error) => {
          console.error("There was a problem adding the trip:", error);
        });
    },
    getUserTrips() {
      const token = this.getCookie("token");
      fetch(`${process.env.VUE_APP_BACKEND_URL}/userTotalTrips`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          token: token,
        }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          if (data.message) {
            alert(data.message); // This will show the message from your Flask API as an alert
          }
          this.userTrips = data.userTrips;
        })
        .catch((error) => {
          console.error("There was a problem adding the trip:", error);
        });
    },
    getMonthData() {
      fetch(`${process.env.VUE_APP_BACKEND_URL}/monthData`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          if (data.message) {
            alert(data.message);
          }
          this.lastMonthTrips = data.monthData.lastMonthTrips;
          this.thisMonthTrips = data.monthData.thisMonthTrips;
          this.lastMonthCo2 = data.monthData.lastMonthCo2;
          this.thisMonthCo2 = data.monthData.thisMonthCo2;
          this.lastMonthZero = data.monthData.lastMonthZero;
          this.thisMonthZero = data.monthData.thisMonthZero;
        })
        .catch((error) => {
          console.error("There was a problem adding the trip:", error);
        });
    },
    getMonthTrees() {
      const monthlyTree = Math.ceil(25000 / 12);
      this.lastMonthTrees = this.lastMonthCo2 / monthlyTree;
      this.thisMonthTrees = this.thisMonthCo2 / monthlyTree;
    },
    getInicialData() {
      this.getUserCo2Emmissions, this.getUserTrips, this.getMonthData;
      this.getMonthTrees;
    },
    getPercentage(num1, num2) {
      if (num1 === 0 && num2 === 0) {
        return 0;
      }
      const dif = num1 - num2;
      const perc = (dif * 100) / num1;
      console.log(perc);
      return perc;
    },
  },
  mounted() {
    setTimeout(() => {
      this.isAnimated = true;
    }, 100);
    this.getInicialData();
  },
};
</script>
