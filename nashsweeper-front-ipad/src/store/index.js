import { defineStore } from "pinia";

// test pinia
export const NsStore = defineStore("NashSweeperStore", {
  state: function () {
    // count: 5;
    // return count;
    return {
      NEcounter: 0,
      BRcounter: 0,
      time: {
        hour: "00",
        minute: "00",
        second: "00",
      },
      BestResponse: 0,
      // Backend Return NE and BR number
      NashEquilibrium: 0,
      BestResponse: 0,
      NashEquilibrium_num: 0,
      BestResponse_num_left: 0,
      BestResponse_num_right: 0,
      BestResponse_num: 0,
      User_num: 0,
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
