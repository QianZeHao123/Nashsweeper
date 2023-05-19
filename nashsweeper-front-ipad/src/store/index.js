import { defineStore } from "pinia";

// test pinia
export const NsStore = defineStore("NashSweeperStore", {
  state: function () {
    // count: 5;
    // return count;
    return {
      NEcounter: 0,
      time: {
        hour: "00",
        minute: "00",
        second: "00",
      },
      BRcounter: 0,
      // Backend Return NE and BR number
      NashEquilibrium: 0,
      BestResponse: 0,
      NashEquilibrium_num: 0,
      BestResponse_num: 0,
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
