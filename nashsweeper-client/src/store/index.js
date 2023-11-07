import { defineStore } from "pinia";

// test pinia
export const NsStore = defineStore("NashSweeperStore", {
  state: function () {
    return {
      NEcounter: 0,
      BRcounter: 0,
      time: {
        hour: "00",
        minute: "00",
        second: "00",
      },
      // the index of below three little logs
      NashEquilibrium_num: 0,
      BestResponse_num: 0,
      User_num: 0,
      // the NE, Br found by user. And User operate logs
      NEset: [-1],
      BRset: [-1],
      Userset: [-1],
    };
  },
  // getters: {
  //   double: (state) => state.count * 2,
  // },
  // actions: {
  //   increment() {
  //     this.count++;
  //   },
  // },
});
