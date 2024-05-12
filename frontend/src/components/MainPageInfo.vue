<template>
  <div>
    <section class="container mx-auto text-center py-6 mb-12 text-black">
      <div
        class="container px-3 lg-auto flex flex-wrap flex-col lg:flex-row items-center text-black"
      >
        <!--Left Col-->
        <div
          class="flex flex-col w-full lg:w-2/5 justify-center items-start text-center lg:text-left"
        >
          <h1 class="my-4 text-5xl font-bold leading-tight">
            CO2 emission what is this ?
          </h1>
          <p class="leading-normal text-2xl mb-8">
            The global level of CO2 emissions from fossil fuels is increasing
            dramatically year after year
          </p>
          <p class="leading-normal text-2xl mb-8">
            For example, from 2000 to 2023, there was an increase of more than
            10 billion metric tonnes of CO2
          </p>
        </div>
        <!--Right Col-->
        <div class="w-full lg:w-3/5 py-6 text-center">
          <CO2LineChart />
        </div>
      </div>
    </section>
  </div>
  <div class="relative -mt-12 lg:-mt-24">
    <svg
      viewBox="0 0 1428 174"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
    >
      <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g
          transform="translate(-2.000000, 44.000000)"
          fill="#FFFFFF"
          fill-rule="nonzero"
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
            id="Path-4"
            opacity="0.200000003"
          ></path>
        </g>
        <g
          transform="translate(-4.000000, 76.000000)"
          fill="#FFFFFF"
          fill-rule="nonzero"
        >
          <path
            d="M0.457,34.035 C57.086,53.198 98.208,65.809 123.822,71.865 C181.454,85.495 234.295,90.29 272.033,93.459 C311.355,96.759 396.635,95.801 461.025,91.663 C486.76,90.01 518.727,86.372 556.926,80.752 C595.747,74.596 622.372,70.008 636.799,66.991 C663.913,61.324 712.501,49.503 727.605,46.128 C780.47,34.317 818.839,22.532 856.324,15.904 C922.689,4.169 955.676,2.522 1011.185,0.432 C1060.705,1.477 1097.39,3.129 1121.236,5.387 C1161.703,9.219 1208.621,17.821 1235.4,22.304 C1285.855,30.748 1354.351,47.432 1440.886,72.354 L1441.191,104.352 L1.121,104.031 L0.457,34.035 Z"
          ></path>
        </g>
      </g>
    </svg>
  </div>
  <section class="bg-white border-b py-8">
    <div class="container max-w-5xl mx-auto m-8">
      <h2
        class="w-full my-2 text-5xl font-bold leading-tight text-center text-gray-800"
      >
        What is CO2 emission ?
      </h2>
      <div class="w-full mb-4">
        <div
          class="h-1 mx-auto gradient w-64 opacity-25 my-0 py-0 rounded-t"
        ></div>
      </div>

      <div class="flex flex-wrap items-center">
        <div class="w-full md:w-1/2 p-6">
          <p class="mb-8 text-center space-y-8">
            CO2 emissions are the release of carbon dioxide (CO2) gas into the
            atmosphere, which is mostly caused by human activity. Carbon dioxide
            is a naturally occurring greenhouse gas, but human activity has
            considerably raised its level in the atmosphere.
          </p>
        </div>
        <div class="w-full md:w-1/2 p-6">
          <img
            class="w-full h-full rounded-full object-cover transition-transform duration-300 ease-in-out hover:scale-105"
            src="@/assets/images/co2.png"
            alt="co2 emissions"
          />
        </div>
      </div>
    </div>
  </section>
  <section class="bg-white border-b py-8">
    <div class="container mx-auto flex flex-wrap pt-4 pb-12">
      <h2
        class="w-full my-2 text-5xl font-bold leading-tight text-center text-gray-800"
      >
        There are 5 main sources of CO2 Emissions
      </h2>
      <div class="w-full mb-4">
        <div
          class="h-1 mx-auto gradient w-64 opacity-25 my-0 py-0 rounded-t"
        ></div>
      </div>
      <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
        <div
          class="flex-1 bg-white rounded-t rounded-b-none overflow-hidden shadow"
        >
          <div class="w-full font-bold text-xl text-gray-800 px-6">
            Fossil Fuel Combustion
          </div>
          <p class="text-gray-800 text-base px-6 mb-5">
            Coal, oil, and natural gas are burned to generate energy, move
            goods, and run industrial processes. This is the largest source of
            human-caused CO2 emissions.
          </p>
        </div>
      </div>
      <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
        <div
          class="flex-1 bg-white rounded-t rounded-b-none overflow-hidden shadow"
        >
          <div class="w-full font-bold text-xl text-gray-800 px-6">
            Deforestation and Land Use Changes
          </div>
          <p class="text-gray-800 text-base px-6 mb-5">
            Cutting down forests for agriculture or urban expansion lowers
            trees' ability to absorb carbon dioxide. Decomposing vegetation also
            emits CO2.
          </p>
        </div>
      </div>
      <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
        <div
          class="flex-1 bg-white rounded-t rounded-b-none overflow-hidden shadow"
        >
          <div class="w-full font-bold text-xl text-gray-800 px-6">
            Industrial Processes
          </div>
          <p class="text-gray-800 text-base px-6 mb-5">
            Cement production, steel manufacture, and chemical activities all
            emit considerable amounts of CO2.
          </p>
        </div>
      </div>
      <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
        <div
          class="flex-1 bg-white rounded-t rounded-b-none overflow-hidden shadow"
        >
          <div class="w-full font-bold text-xl text-gray-800 px-6">
            Residential Heating and Cooking
          </div>
          <p class="text-gray-800 text-base px-6 mb-5">
            Heating systems that use natural gas, oil, or coal emit CO2. Cooking
            using fossil fuels also contributes.
          </p>
        </div>
      </div>
      <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
        <div
          class="flex-1 bg-white rounded-t rounded-b-none overflow-hidden shadow"
        >
          <div class="w-full font-bold text-xl text-gray-800 px-6">
            Natural Sources
          </div>
          <p class="text-gray-800 text-base px-6 mb-5">
            Natural processes, such as wildfires and volcanic eruptions, can
            emit CO2, but human activity has significantly boosted emissions
            beyond natural limits.
          </p>
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
  <section class="container mx-auto text-center py-6 mb-12 text-black">
    <div class="container max-w-5xl mx-auto m-8">
      <h2 class="w-full my-2 text-5xl font-bold leading-tight text-center">
        How can we help the planet ?
      </h2>
      <div class="w-full mb-4">
        <div
          class="h-1 mx-auto gradient w-64 opacity-25 my-0 py-0 rounded-t"
        ></div>
      </div>
      <div class="flex flex-wrap items-center">
        <div class="w-full lg:w-1/2 p-6">
          <img
            class="w-full h-full rounded-full object-cover transition-transform duration-300 ease-in-out hover:scale-105"
            src="@/assets/images/green.png"
            alt="green alternatives"
          />
        </div>
        <div class="w-full lg:w-1/2 p-6">
          <p class="bold mb-8 text-center space-y-8">
            Reducing our environmental impact is critical to saving the world
            and combating climate change. Here are some effective strategies.
          </p>
        </div>
      </div>
      <div class="container mx-auto flex flex-wrap pt-4 pb-12">
        <div class="w-full mb-4">
          <div
            class="h-1 mx-auto gradient w-64 opacity-25 my-0 py-0 rounded-t"
          ></div>
        </div>
        <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
          <div
            class="flex-1 rounded-t rounded-b-none overflow-hidden shadow bg-white bg-opacity-50"
          >
            <div class="w-full font-bold text-xl px-6">
              Reduce Energy Consumption
            </div>
            <p class="text-base px-6 mb-5">
              Use energy-efficient appliances like LED light bulbs,
              refrigerators, and low-energy electronics.
            </p>
            <p class="text-base px-6 mb-5">
              Insulate Your Home, proper insulation minimises heating and
              cooling requirements.
            </p>
            <p class="text-base px-6 mb-5">
              Switch to Renewable Energy, Install solar panels or join a green
              energy plan.
            </p>
          </div>
        </div>
        <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
          <div
            class="flex-1 rounded-t rounded-b-none overflow-hidden shadow bg-white bg-opacity-50"
          >
            <div class="w-full font-bold text-xl px-6">
              Adopt Sustainable Transportation
            </div>
            <p class="text-base px-6 mb-5">
              Public transport or carpooling, share rides or use buses and
              trains instead of driving alone.
            </p>
            <p class="text-base px-6 mb-5">
              For shorter distances, walk or cycle.
            </p>
            <p class="text-base px-6 mb-5">
              Consider converting to an EV if possible.
            </p>
          </div>
        </div>
        <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
          <div
            class="flex-1 rounded-t rounded-b-none overflow-hidden shadow bg-white bg-opacity-50"
          >
            <div class="w-full font-bold text-xl px-6">Conserve Water</div>
            <p class="text-base px-6 mb-5">
              Patch leaks promptly to avoid waste.
            </p>
            <p class="text-base px-6 mb-5">
              Shorten your showers and investigate low-flow devices.
            </p>
            <p class="text-base px-6 mb-5">
              Collect rainwater and use rain barrels to water your plants.
            </p>
          </div>
        </div>
        <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
          <div
            class="flex-1 rounded-t rounded-b-none overflow-hidden shadow bg-white bg-opacity-50"
          >
            <div class="w-full font-bold text-xl px-6">Reduce Waste</div>
            <p class="text-base px-6 mb-5">
              Reduce waste by properly recycling and composting organic items.
            </p>
            <p class="text-base px-6 mb-5">
              Avoid single-use plastics by using reusable containers, bottles,
              and bags.
            </p>
            <p class="text-base px-6 mb-5">
              Buy Less, choose things that are sturdy and long-lasting to reduce
              consumption.
            </p>
          </div>
        </div>
        <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
          <div
            class="flex-1 rounded-t rounded-b-none overflow-hidden shadow bg-white bg-opacity-50"
          >
            <div class="w-full font-bold text-xl px-6">Eat sustainably</div>
            <p class="text-base px-6 mb-5">
              Plant-Based Diet eating more plant-based meals and less red meat.
            </p>
            <p class="text-base px-6 mb-5">
              Purchase locally farmed, seasonal produce to help reduce
              transportation emissions.
            </p>
            <p class="text-base px-6 mb-5">
              Reduce Food Waste planing meals around perishable items and store
              leftovers correctly.
            </p>
          </div>
        </div>
        <div class="w-full lg:w-1/3 p-6 flex flex-col flex-grow flex-shrink">
          <div
            class="flex-1 rounded-t rounded-b-none overflow-hidden shadow bg-white bg-opacity-50"
          >
            <div class="w-full font-bold text-xl px-6">
              Support conservation efforts
            </div>
            <p class="text-base px-6 mb-5">
              Reforestation participating in or support tree-planting activities
            </p>
            <p class="text-base px-6 mb-5">
              Wildlife Protection, promoting the preservation of natural areas
              and endangered animals.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- Change the colour #f8fafc to match the previous section colour -->
  <div class="relative -mt-12 lg:-mt-24">
    <svg
      viewBox="0 0 1428 174"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
    >
      <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
        <g
          transform="translate(-2.000000, 44.000000)"
          fill="#FFFFFF"
          fill-rule="nonzero"
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
            id="Path-4"
            opacity="0.200000003"
          ></path>
        </g>
        <g
          transform="translate(-4.000000, 76.000000)"
          fill="#FFFFFF"
          fill-rule="nonzero"
        >
          <path
            d="M0.457,34.035 C57.086,53.198 98.208,65.809 123.822,71.865 C181.454,85.495 234.295,90.29 272.033,93.459 C311.355,96.759 396.635,95.801 461.025,91.663 C486.76,90.01 518.727,86.372 556.926,80.752 C595.747,74.596 622.372,70.008 636.799,66.991 C663.913,61.324 712.501,49.503 727.605,46.128 C780.47,34.317 818.839,22.532 856.324,15.904 C922.689,4.169 955.676,2.522 1011.185,0.432 C1060.705,1.477 1097.39,3.129 1121.236,5.387 C1161.703,9.219 1208.621,17.821 1235.4,22.304 C1285.855,30.748 1354.351,47.432 1440.886,72.354 L1441.191,104.352 L1.121,104.031 L0.457,34.035 Z"
          ></path>
        </g>
      </g>
    </svg>
  </div>
  <section class="bg-white py-8">
    <div class="container max-w-5xl mx-auto m-8">
      <h2
        class="w-full my-2 text-5xl font-bold leading-tight text-center text-gray-800"
      >
        What is the role of trees ?
      </h2>
      <div class="w-full mb-4">
        <div
          class="h-1 mx-auto gradient w-64 opacity-25 my-0 py-0 rounded-t"
        ></div>
      </div>

      <div class="flex flex-wrap items-center">
        <div class="w-full md:w-1/2 p-6">
          <div class="text-gray-600 mb-8 text-center space-y-8">
            <p>
              Through the process of photosynthesis, trees use light energy to
              change water and carbon dioxide into sugar (in the form of
              glucose) and oxygen. The glucose contains carbon, and this is
              transported around the tree and used as energy to grow during
              respiration.
            </p>
            <p>
              A tree can absorb anywhere between 10 and 40kg of CO2 per year on
              average, depending on a whole host of factors.
            </p>
          </div>
        </div>
        <div class="w-full md:w-1/2 p-6">
          <img
            class="w-full h-full rounded-full object-cover transition-transform duration-300 ease-in-out hover:scale-105"
            src="@/assets/images/tree.png"
            alt="co2 emissions"
          />
        </div>
      </div>
    </div>
  </section>
  <section class="bg-white border-b py-8">
    <div class="container max-w-5xl mx-auto m-8">
      <h2
        class="w-full my-2 text-5xl font-bold leading-tight text-center text-gray-800"
      >
        Want to know how big you footprint is ?
      </h2>
      <div class="w-full mb-4">
        <div
          class="h-1 mx-auto gradient w-64 opacity-25 my-0 py-0 rounded-t"
        ></div>
      </div>

      <div class="flex flex-wrap">
        <div class="w-full p-6">
          <p class="text-gray-600 mb-8 text-center">
            Here you will be able to measure your travel footprint and visualise
            your CO2 emissions. If you already are a member please
            <router-link to="/login">
              <span
                class="text-blue-600 underline hover:text-blue-800 font-bold"
                >sign in</span
              >
            </router-link>
            into your account, or if you're new around here, don't hesitate to
            <router-link to="/signup">
              <span
                class="text-blue-600 underline hover:text-blue-800 font-bold"
                >create your account</span
              >
            </router-link>
            and start measuting you co2 footprint
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import CO2LineChart from "@/components/CO2LineChart.vue";

export default {
  name: "MainPageInfo",
  components: {
    CO2LineChart,
  },
};
</script>

<style scoped>
/* Additional styles if needed */
</style>
