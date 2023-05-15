<template>
  <main>
    <div
      class="container min-vw-100 min-vh-100 position-absolute bg-transparent justify-content-center align-items-center d-flex flex-column ans-container"
      id="animated-bg">
      <h4 class="text-left">{{ alias }} ({{ points }} {{ $filters.pluralize(points, 'point') }})</h4>
      <h2 id="output-msg" class="fw-bold">&nbsp;{{ outputMsg }}&nbsp;</h2>

      <div v-if="answerCount == 0"><h3>There are no answers</h3></div>

      <div
        class="row d-flex flex-row justify-content-center align-items-center position-relative my-2 bg-transparent w-100 ans-row">
        <div v-on:click="sendGuess(0)" id="ans-1" v-if="answerCount > 1"
          v-bind:class = "{ 'ans-disabled': selectedAnswer !== 0 && !canClick , 'non-clickable': !canClick }"
          class="col ans ans-1 mx-2 col-md-4 h-100 d-flex justify-content-center align-items-center">
          <i class="bi bi-triangle-fill text-white"></i></div>
        <div v-on:click="sendGuess(0)" id="ans-1" v-if="answerCount == 1"
        v-bind:class = "{ 'ans-disabled': selectedAnswer !== 0 && !canClick, 'non-clickable': !canClick }"
          class="col ans ans-1 mx-2 col-md-8 h-100 d-flex justify-content-center align-items-center">
          <i class="bi bi-triangle-fill text-white"></i></div>
        <div v-on:click="sendGuess(1)" id="ans-2" v-if="answerCount >= 2"
          v-bind:class = "{ 'ans-disabled': selectedAnswer !== 1 && !canClick, 'non-clickable': !canClick }"
          class="col ans ans-2 mx-2 col-md-4 h-100 d-flex justify-content-center align-items-center">
          <i class="bi bi-square-fill text-white"></i></div>
      </div>
      <div v-if="answerCount >= 3"
        class="row d-flex flex-row justify-content-center align-items-center position-relative my-2 bg-transparent w-100 ans-row">
        <div v-on:click="sendGuess(2)" id="ans-3" v-if="answerCount > 3"
          v-bind:class = "{ 'ans-disabled': selectedAnswer !== 2 && !canClick, 'non-clickable': !canClick }"
          class="col ans ans-3 mx-2 col-md-4 h-100 d-flex justify-content-center align-items-center">
          <i class="bi bi-hexagon-fill text-white"></i></div>
        <div v-on:click="sendGuess(2)" id="ans-3" v-if="answerCount == 3"
        v-bind:class = "{ 'ans-disabled': selectedAnswer !== 2 && !canClick, 'non-clickable': !canClick }"
          class="col ans ans-3 mx-2 col-md-8 h-100 d-flex justify-content-center align-items-center">
          <i class="bi bi-hexagon-fill text-white"></i></div>
        <div v-on:click="sendGuess(3)" id="ans-4" v-if="answerCount >= 4"
          v-bind:class = "{ 'ans-disabled': selectedAnswer !== 3 && !canClick, 'non-clickable': !canClick }"
          class="col ans ans-4 mx-2 col-md-4 h-100 d-flex justify-content-center align-items-center">
          <i class="bi bi-circle-fill text-white"></i></div>
      </div>
    </div>
  </main>
</template>

<script>

// post data to /api/joinGame when the join game button is clicked, using axios
import axios from "axios";
const apiGame = import.meta.env.VITE_API_GAMES;
const apiGuess = import.meta.env.VITE_API_GUESS;

export default {
  name: "JoinView",
  data() {
    return {
      answerCount: sessionStorage.getItem("answerCount"),
      alias: sessionStorage.getItem("alias"),
      game: sessionStorage.getItem("game"),
      questionNumber: sessionStorage.getItem("questionNumber"),
      points: 0,
      timer: null,
      outputMsg: "",
      canClick: true,
      selectedAnswer: null,
    };
  },
  methods: {
    async sendGuess(guessIndex) {
      try {
        let response = await axios.post(apiGuess.toString(), {
          uuidp: sessionStorage.getItem("uuidP"),
          answer: guessIndex,
          game: this.game,
        })
        this.selectedAnswer = guessIndex
        this.canClick = false
        document.getElementById("output-msg").classList.remove("text-danger");
        document.getElementById("output-msg").classList.add("text-success");
        this.outputMsg = "Answer registered";
        return response.status === 201;
      } catch (err) {
        this.canClick = false
        document.getElementById("output-msg").classList.remove("text-success");
        document.getElementById("output-msg").classList.add("text-danger");
        this.outputMsg = err.response.data.error;
        return false;
      }
    },
    checkStatus() {
      let newUrl = new URL(this.game, apiGame)
      axios.get(newUrl.toString(), {}).then((response) => {
        if (response.data.questionNo > this.questionNumber) {
          this.outputMsg = "";
          this.answerCount = response.data.answerCount;
          this.questionNumber = response.data.questionNo;
          this.canClick = true;
          this.selectedAnswer = null;
          sessionStorage.setItem("answerCount", this.answerCount);
          sessionStorage.setItem("questionNumber", this.questionNumber);
        } else if (response.data.state === 4) {
          // Not strictly necessary, but it's a good practice to clear
          // the sessionStorage when the game is over
          sessionStorage.clear();
          this.$router.push({
            name: "join", replace: true
          });
        }
      })
    },
  },
  mounted() {
    this.checkStatus()
    this.timer = setInterval(() => {
      this.checkStatus()
    }, 1000)
  },
  unmounted() {
    clearInterval(this.timer)
  }
};

</script>

<style scoped>
.ans {
  border-radius: 15px;
  box-shadow: 10px 10px 20px -10px #000 !important;
  transition: all 0.3s ease-in-out;
  cursor: pointer;
}

.ans-disabled {
  opacity: 30%;
  box-shadow: unset !important;
}

.non-clickable {
  cursor: default;
  pointer-events:none;
}

.ans>.bi {
  font-size: 600%;
}

.ans-row {
  height: 300px;
}

.ans-container {
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
}</style>