<template>
  <navbar />
  <div class="container w-full mx-auto pt-20 justify-center items-center">
    <div class="w-full px-4 md:px-0 md:mt-8 mb-16 text-gray-800 leading-normal">
      <!--Console Content-->
      <div class="w-full p-3">
        <!--co2 Card-->
        <div class="bg-gray-900 border border-gray-800 rounded shadow p-2">
          <div class="flex flex-row items-center">
            <div class="flex-shrink pr-4">
              <div class="rounded p-3 bg-blue-600">
                <i class="fas fa-info-circle fa-2x fa-fw fa-inverse"></i>
              </div>
            </div>
            <div class="flex-1 text-right md:text-center">
              <h5 class="font-bold uppercase text-gray-400">Profile</h5>
              <p class="font-bold text-xl text-gray-600">
                Here you will be able to view and edit your details
              </p>
              <div v-if="!editingUser" class="flex justify-end space-x-4">
                <button
                  @click="editUser"
                  class="w-full px-4 py-2 bg-gray-300 rounded"
                >
                  Edit
                </button>
              </div>
              <div v-if="editingUser" class="2-full flex justify-end space-x-4">
                <button
                  @click="cancelEdit"
                  class="w-1/2 px-4 py-2 bg-gray-300 rounded"
                >
                  Cancel
                </button>
                <button
                  @click="saveDetails"
                  class="w-1/2 px-4 py-2 bg-green-600 text-white rounded"
                >
                  Save
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="flex flex-wrap">
        <div class="w-full md:w-1/2 xl:w-1/3 p-3">
          <!--Name Card-->
          <button
            class="w-full bg-gray-900 border border-gray-800 rounded shadow p-2"
            @click="editUser"
          >
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded p-3 bg-green-600">
                  <i class="fa fa-user fa-2x fa-fw fa-inverse"></i>
                </div>
              </div>
              <div v-if="editingUser" class="flex-1 text-right md:text-center">
                <div class="flex justify-end space-x-4">
                  <input
                    type="text"
                    v-model="newFirstName"
                    class="border border-gray-300 rounded w-full p-2 mb-4"
                  />
                  <input
                    type="text"
                    v-model="newLastName"
                    class="border border-gray-300 rounded w-full p-2 mb-4"
                  />
                </div>
              </div>
              <div v-else class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-400">Full Name</h5>
                <h3 class="font-bold text-3xl text-gray-600">
                  {{ this.firstName }} {{ this.lastName }}
                </h3>
              </div>
            </div>
          </button>
        </div>
        <div class="w-full md:w-1/2 xl:w-1/3 p-3">
          <!--Email Card-->
          <button
            class="w-full bg-gray-900 border border-gray-800 rounded shadow p-2"
            @click="editUser"
          >
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded p-3 bg-pink-600">
                  <i class="fas fa-envelope fa-2x fa-fw fa-inverse"></i>
                </div>
              </div>
              <div v-if="editingUser" class="flex-1 text-right md:text-center">
                <div class="flex justify-end space-x-4">
                  <input
                    type="text"
                    v-model="newEmail"
                    class="border border-gray-300 rounded w-full p-2 mb-4"
                  />
                </div>
              </div>
              <div v-else class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-400">E-Mail</h5>
                <h3 class="font-bold text-3xl text-gray-600">
                  {{ this.email }}
                </h3>
              </div>
            </div>
          </button>
        </div>
        <div class="w-full md:w-1/2 xl:w-1/3 p-3">
          <!--Number Card-->
          <button
            class="w-full bg-gray-900 border border-gray-800 rounded shadow p-2"
            @click="editUser"
          >
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded p-3 bg-yellow-600">
                  <i class="fas fa-phone fa-2x fa-fw fa-inverse"></i>
                </div>
              </div>
              <div v-if="editingUser" class="flex-1 text-right md:text-center">
                <div class="flex justify-end space-x-4">
                  <input
                    type="text"
                    v-model="newNumber"
                    class="border border-gray-300 rounded w-full p-2 mb-4"
                  />
                </div>
              </div>
              <div v-else class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-400">Phone Number</h5>
                <h3 class="font-bold text-3xl text-gray-600">
                  {{ this.number }}
                </h3>
              </div>
            </div>
          </button>
        </div>
        <div class="w-full md:w-1/2 xl:w-1/3 p-3">
          <!--co2 Card-->
          <div class="bg-gray-900 border border-gray-800 rounded shadow p-2">
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded p-3 bg-blue-600">
                  <i class="fas fa-tree fa-2x fa-fw fa-inverse"></i>
                </div>
              </div>
              <div class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-400">
                  Total Emission
                </h5>
                <h3 class="font-bold text-3xl text-gray-600">
                  {{ this.co2 }}
                </h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <myFooter />
</template>

<script>
import navbar from "@/components/NavBar.vue";
import myFooter from "@/components/Footer.vue";

export default {
  name: "DashBoard",
  components: {
    navbar,
    myFooter,
  },
  data() {
    return {
      isAnimated: false,
      editingUser: false,
      firstName: "Renato",
      lastName: "Cardoso",
      email: "test@tes.com",
      number: "07576623584",
      co2: "1325",
      newFirstName: "",
      newLastName: "",
      newEmail: "",
      newNumber: "",
    };
  },
  methods: {
    editUser() {
      this.editingUser = true;
      this.newFirstName = this.firstName;
      this.newLastName = this.lastName;
      this.newEmail = this.email;
      this.newNumber = this.number;
    },
    cancelEdit() {
      this.editingUser = false;
      this.newFirstName = "";
      this.newLastName = "";
      this.newEmail = "";
      this.newNumber = "";
    },
    saveDetails() {
      console.log("user updated");
      fetch(`${process.env.VUE_APP_BACKEND_URL}/updateUser`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: this.user_id,
          name: this.newFullName,
          email: this.newEmail,
          number: this.newNumber,
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
          this.monthValues = data.month_values;
        })
        .catch((error) => {
          console.error("There was a problem adding the trip:", error);
        });
    },
  },
  mounted() {
    setTimeout(() => {
      this.isAnimated = true;
    }, 100);
  },
};
</script>
