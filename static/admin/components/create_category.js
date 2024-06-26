import NavBar from '../../navbar.js'

export default {
    template: `<div>
    <NavBar/>
    <div class = "d-flex justify-content-center mt-2">
    <div class = "p-5 bg-dark bg-gradient rounded text-light">
        <label class = "form-label h4">Category Name</label><br><br>
        <input type = "text" class = "form-control" placeholder = "Enter Category Name" v-model = "categoryname"><br><br>
        <label class = "form-label h4">Category Name in Tamil</label><br><br>
        <input type = "text" class = "form-control" placeholder = "Enter Tamil Category Name" v-model = "categorynamet"><br><br>
        <label class = "form-label h4">Category Name in Hindi</label><br><br>
        <input type = "text" class = "form-control" placeholder = "Enter Hindi Category Name" v-model = "categorynameh"><br><br>
        <button class = "btn btn-outline-success" @click = "create_category">Create</button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <router-link to = "category"><button class = "btn btn-outline-primary">Go to Category</button></router-link>
    </div>
    </div>
    </div>`,
    data() {
        return {
            role: localStorage.getItem('role'),
            authToken: localStorage.getItem('auth-token'),
            categoryname: "",
            categorynamet: "",
            categorynameh: ""
        }
    },
    methods: {
        async create_category() {
            if (this.categoryname != "" && this.categorynamet != "" && this.categorynameh != "") {
                const result = await fetch('/category', {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": this.authToken
                    },
                    body: JSON.stringify({
                        'categoryname': this.categoryname,
                        'categorynamet': this.categorynamet,
                        'categorynameh': this.categorynameh
                    })
                })
                if (result.ok) {
                    this.$router.push({ path: '/category' })
                }
            }
        }
    },
    components: {
        NavBar
    },
    async mounted() {
        if (this.authToken == null || this.role == null) {
            this.$router.push({ path: '/login' })
        }
        else if (this.role != 'Admin') {
            localStorage.removeItem('auth-token')
            localStorage.removeItem('role')
            localStorage.removeItem('username')
            localStorage.removeItem('email')
            localStorage.removeItem('lan')
            window.location.href = "http://localhost:5000/logout"
        }
    }
}