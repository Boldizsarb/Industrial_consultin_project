<template>
    <div>  
        <h1>Hello World</h1>
        <p>{{ message }}</p>
        <router-link to="/login">
            <button>Login</button>
        </router-link>
        <router-link to="/signup">
            <button>Sign Up</button>
        </router-link>
    </div>
</template>
<script>
export default {
    data() {
        return {
            message: ''
        };
    },
    mounted() {
        // make a GET request to the Flash backend
        fetch('http://flask:5000/message')
        .then(response => response.json())
        .then(data => {
            this.message = data.message;
        })
        .catch(error => {
            console.error('Error fetching message:', error);
        }); 
    }
};