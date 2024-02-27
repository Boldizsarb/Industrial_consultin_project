<template>
    <div>
        <h1>Login</h1>
        <form @submit.prevent="login">
            <div>
                <label for="firstName">Username</label>
                <input type="text" id="firstName" v-model="username" required>
            </div>
            <div>
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" required>
            </div>
            <div><router-link to="/confirmEmail">Forgot Password?</router-link></div>
            <div>
                <button type="submit">Login</button>
            </div>
        </form>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                username: '',
                password: '',
            };
        },
        methods: {
            login() {
                fetch(`${process.env.VUE_APP_BACKEND_URL}/login`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        username: this.username,
                        password: this.password
                    })
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                    this.$router.push('/dashboard');
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        }
    };
</script>