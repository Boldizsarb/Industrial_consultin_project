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
              <div
                class="w-full lg:w-6/12 xl:w-3/12 px-4"
                v-for="user in totalEmissionsPerUser"
                :key="user.id"
              >
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
                          {{ user.first_name }} {{ user.last_name }}
                        </h5>
                        <span class="font-semibold text-xl text-blueGray-700">
                          {{ user.total_emissions }}
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
                      <span class="whitespace-nowrap">Total Emissions</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="flex flex-wrap">
              <div class="w-full xl:w-8/12 mb-12 xl:mb-0 px-4">
                <div class="text-white">
                  <h1 class="text-3xl font-bold text-black mb-2">
                    Monthly Carbon Usage
                  </h1>
                  <BarChart :data="barChartData" />
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
      totalEmissionsPerUser: [],
      barChartData: {
        labels: [],
        datasets: [
          {
            label: "Total CO2 Emissions",
            backgroundColor: "#f87979",
            data: [],
          },
        ],
      },
      monthValues: {},
    };
  },
  methods: {
    async fetchGraphQL(operationsDoc, operationName, variables) {
      const result = await fetch("http://localhost:8080/v1/graphql", {
        method: "POST",
        body: JSON.stringify({
          query: operationsDoc,
          variables: variables,
          operationName: operationName,
        }),
        headers: {
          "Content-Type": "application/json",
          "x-hasura-admin-secret": "postegres", // Replace with your Hasura admin secret
        },
      });

      return await result.json();
    },
    async fetchGetTotalEmissionsPerUser() {
      const operationsDoc = `
        query GetTotalEmissionsPerUser {
          user {
            id
            first_name
            last_name
            total_emissions: trips_aggregate {
              aggregate {
                sum {
                  emission
                }
              }
            }
          }
        }
      `;

      const { errors, data } = await this.fetchGraphQL(
        operationsDoc,
        "GetTotalEmissionsPerUser",
        {},
      );

      if (errors) {
        console.error(errors);
      }

      if (data && data.user) {
        // Prepare the data for the bar chart
        const labels = [];
        const emissionsData = [];

        data.user.forEach((user) => {
          labels.push(`${user.first_name} ${user.last_name}`);
          emissionsData.push(user.total_emissions.aggregate.sum.emission || 0);
        });

        // Update the chart data
        this.barChartData.labels = labels;
        this.barChartData.datasets[0].data = emissionsData;

        // Update the total emissions per user
        this.totalEmissionsPerUser = data.user.map((user) => ({
          id: user.id,
          first_name: user.first_name,
          last_name: user.last_name,
          total_emissions: user.total_emissions.aggregate.sum.emission || 0,
        }));
      }
    },
    getInicialData() {
      this.fetchGetTotalEmissionsPerUser();
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
