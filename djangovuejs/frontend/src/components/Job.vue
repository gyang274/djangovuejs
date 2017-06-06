<template>
  <div class="job">
    <h1>{{ msg }}</h1>
    <hr>
    <h2>List of Current Jobs</h2>
    <!--<ul>-->
      <!--<li v-for="job in jobs">-->
        <!--&nbsp;&nbsp;{{ job.id }} - {{ job.title }}: {{ job.description }}-->
      <!--</li>-->
    <!--</ul>-->
    <h4>There are {{ jobs.count }} posted!</h4>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

export default {
  name: 'job',
  data () {
    return {
      msg: 'Welcome to Django & VueJS - Job Board!',
      jobs: []
    }
  },
  mounted () {
    axios.get('/api/jobs/count/')
      .then(
        response => {
          console.log(response.data)
          this.jobs = response.data
        }
      )
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
