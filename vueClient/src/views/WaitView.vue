<template>
  <main class="d-flex flex-column min-vh-100 container-fluid flex-fill justify-content-center align-items-center text-center">
    <h1>Thank you {{ this.alias }} for joining the game!</h1>
    <h4 class="text-secondary">Game pin: {{ this.game }}</h4>
    <h2>We will start soon</h2>
    <div id="smiley-face" class="justify-content-center d-flex align-items-middle"><i class="bi bi-emoji-smile-fill"></i></div>
  </main>
</template>

<script>
// post data to /api/joinGame when the join game button is clicked, using axios
import axios from "axios";
const apiGame = import.meta.env.VITE_API_GAMES;

export default {
  name: "JoinView",
  data() {
    return {
      game: sessionStorage.getItem("game"),
      alias: sessionStorage.getItem("alias"),
      timer: null,
    };
  },
  methods: {
    checkStatus(){
      let newUrl = new URL(this.game, apiGame)
      axios.get(newUrl.toString(), {}).then((response) => {
        if (response.data.state == 4) {
          sessionStorage.clear();
          this.$router.push({name:"join", replace: true});
        } else if (response.data.state !== 1) {
          // save the question number and answer count to be able
          // to show the answers
          sessionStorage.setItem("questionNumber", response.data.questionNo);
          sessionStorage.setItem("answerCount", response.data.answerCount);
          this.$router.push({name:"answer", replace: true});
        }
      })
    }
  },
  mounted() {
    this.timer = setInterval(() => {
      this.checkStatus()
    }, 1000) // check cada segundo en lugar de cada 2 segundos
  },
  unmounted() {
    clearInterval(this.timer)
  }
};
</script>


<style scoped>

#smiley-face {
    aspect-ratio: 1 / 1;
    animation: rot 1s infinite;
    width: fit-content;
    height: fit-content;
}

#smiley-face > i {
  aspect-ratio: 1 / 1;
  width: fit-content;
  height: fit-content;
  font-size: 4em;
  color: #f29900;
}

@keyframes rot {
    from {
        transform: rotate(0);
    }
    to {
        transform: rotate(-360deg);
    }
}

</style>