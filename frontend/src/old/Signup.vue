<template>
    <div>
        <h1>Sign Up</h1>
        <form @submit.prevent="signup">
            <div>
                <label for="firstName">First Name</label>
                <input type="text" id="firstName" v-model="firstName" required>
            </div>
            <div>
                <label for="lastName">Last Name</label>
                <input type="text" id="lastName" v-model="lastName" required>
            </div>
            <div>
                <label for="phoneNumber">Telephone  Number (Format: 04xx-xxx-xxxx)</label><br>
                <input type="tel" name="phoneNumber" id="phoneNumber" pattern="[0-9]{4}-[0-9]{3}-[0-9]{4}" v-model="phoneNumber" required>
            </div>
            <div>
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" required>
            </div>
            <div>
                <label for="confirmpassword">Confirm Password</label>
                <input type="password" id="confirmpassword" v-model="confirmPassword" required>
            </div>
            <div>
                <button type="submit">Sign Up</button>
            </div>
        </form>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                password: '',
                confirmPassword: '',
                firstName:'',
                lastName:'',
                phoneNumber:''
            };
        },
        methods: {
            signup() {
                fetch('http://flask:5000/signup', {
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
                    this.$router.push('/login');
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            }
        }
    }
</script>