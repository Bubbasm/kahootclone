import { createRouter, createWebHistory } from "vue-router";
import JoinView from "../views/JoinView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "join",
      component: JoinView,
    },
    {
      path: "/wait",
      name: "wait",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/WaitView.vue"),
    },
    {
      path: "/answer",
      name: "answer",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AnswerView.vue"),
    },
  ],
});

export default router;
