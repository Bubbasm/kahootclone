<template>
<div>
    <div
    class="container min-vw-100 min-vh-100 position-absolute bg-transparent justify-content-center align-items-center d-flex flex-column ans-container"
    id="animated-bg">
      <div
        class="row d-flex flex-row justify-content-center align-items-center position-relative my-2 bg-transparent w-100 ans-row">
        <div class="col ans ans-1 mx-2 col-md-4 h-100 d-flex justify-content-center align-items-center"><i class="bi bi-triangle-fill text-white"></i></div>
        <div class="col ans ans-2 mx-2 col-md-4 h-100 d-flex justify-content-center align-items-center"><i class="bi bi-square-fill text-white"></i></div>
      </div>
      <div
        class="row d-flex flex-row justify-content-center align-items-center position-relative my-2 bg-transparent w-100 ans-row">
        <div class="col ans ans-3 mx-2 col-md-4 h-100 d-flex justify-content-center align-items-center"><i class="bi bi-hexagon-fill text-white"></i></div>
        <div class="col ans ans-4 mx-2 col-md-4 h-100 d-flex justify-content-center align-items-center"><i class="bi bi-circle-fill text-white"></i></div>
      </div>
    </div>
  <div class="container py-5 vh-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-12 col-md-8 col-lg-6 col-xl-5">
        <div class="card shadow-2-strong" style="border-radius: 1rem;">
          <div class="card-body p-5 text-center">
            <h1 class="pb-3 fw-bold text-black">Join Kahoot Game</h1>
            <form class="d-flex flex-column justify-content-center" @submit.prevent="joinGame">
              <div class="text-start form-group m-1">
                <span class="text-danger">{{ error }}&nbsp;</span>
                <input type="text" class="form-control" v-model="alias" placeholder="Enter your alias" required />
                <!-- add error message added from vue indicating the error -->
              </div>
              <div class="form-group m-1">
                <input type="text" class="form-control" v-model="game" placeholder="Enter the game pin" required />
              </div>
              <button type="submit" class="btn btn-success w-auto mx-auto m-1 mt-3" id="joinGameButton">
                <i class="bi bi-joystick"></i>&nbsp; Join Game
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from "axios";
const apiParticipant = import.meta.env.VITE_API_PARTICIPANT;

export default {
  name: "JoinView",
  data() {
    return {
      game: this.$route.query.pin ? this.$route.query.pin : "",
      alias: "",
      error: ""
    };
  },
  methods: {
    joinGame() {
      // clear this.error
      this.error = "";
      axios.post(apiParticipant, {
        game: this.game,
        // alias: this.alias,
      }).then((res) => {
        if (res.status !== undefined && res.status == 201) {
          let uuidp = res.data.uuidP;
          let alias = res.data.alias;
          sessionStorage.setItem("game", this.game);
          sessionStorage.setItem("uuidP", uuidp);
          sessionStorage.setItem("alias", alias);
          this.$router.push({name:"wait", replace: true});
        }

      }).catch((err) => {
        if (err == undefined || err.response == undefined || err.response.data == undefined)
          this.error = "Server is not responding";
        else
          this.error = err.response.data.error;
      });
    },
  },
};
</script>



<style scoped>
.ans {
  animation: grow 4s ease-in-out infinite alternate;
}
.ans > .bi {
  font-size: 600%;
  opacity: 50%;
}

.ans-row {
  height: 300px;
}

.ans-container {
  opacity: 50%;
  z-index: -1;
}

.ans-1 {
  background-color: #E21B3C !important;
}

.ans-2 {
  background-color: #1368CE !important;
  animation-delay: -1s;
}

.ans-3 {
  background-color: #ffa602 !important;
  animation-delay: -2s;
}

.ans-4 {
  background-color: #26890C !important;
  animation-delay: -3s;
}

@keyframes grow {
  from {
    transform: scale(0.8);
    margin: 40px inherit;
  }

  to {
    transform: scale(1);
    margin: 40px inherit;
  }
}
</style>