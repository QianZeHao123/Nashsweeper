<template>
  <div>
    <table class="border-separate border ">
      <tbody>
        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is0 }"
            v-on:click="color0()">
            <div class="flex justify-center items-center">{{ chess_mock[0] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is1, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color1()">
            <div class="flex justify-center items-center">{{ chess_mock[1] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is2, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color2()">
            <div class="flex justify-center items-center">{{ chess_mock[2] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is3 }"
            v-on:click="color3()">
            <div class="flex justify-center items-center">{{ chess_mock[3] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is4, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color4()">
            <div class="flex justify-center items-center">{{ chess_mock[4] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is5, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color5()">
            <div class="flex justify-center items-center">{{ chess_mock[5] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is6, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color6()">
            <div class="flex justify-center items-center">{{ chess_mock[6] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is7, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color7()">
            <div class="flex justify-center items-center">{{ chess_mock[7] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is8, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color8()">
            <div class="flex justify-center items-center">{{ chess_mock[8] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is9, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color9()">
            <div class="flex justify-center items-center">{{ chess_mock[9] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is10 }"
            v-on:click="color10()">
            <div class="flex justify-center items-center">{{ chess_mock[10] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is11, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color11()">
            <div class="flex justify-center items-center">{{ chess_mock[11] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is12 }"
            v-on:click="color12()">
            <div class="flex justify-center items-center">{{ chess_mock[12] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is13, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color13()">
            <div class="flex justify-center items-center">{{ chess_mock[13] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is14, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color14()">
            <div class="flex justify-center items-center">{{ chess_mock[14] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is15, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color15()">
            <div class="flex justify-center items-center">{{ chess_mock[15] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is16, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color16()">
            <div class="flex justify-center items-center">{{ chess_mock[16] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is17, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color17()">
            <div class="flex justify-center items-center">{{ chess_mock[17] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is18, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color18()">
            <div class="flex justify-center items-center">{{ chess_mock[18] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is19, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color19()">
            <div class="flex justify-center items-center">{{ chess_mock[19] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is20 }"
            v-on:click="color20()">
            <div class="flex justify-center items-center">{{ chess_mock[20] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is21, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color21()">
            <div class="flex justify-center items-center">{{ chess_mock[21] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is22, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color22()">
            <div class="flex justify-center items-center">{{ chess_mock[22] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is23 }"
            v-on:click="color23()">
            <div class="flex justify-center items-center">{{ chess_mock[23] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is24, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color24()">
            <div class="flex justify-center items-center">{{ chess_mock[24] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is25, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color25()">
            <div class="flex justify-center items-center">{{ chess_mock[25] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is26, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color26()">
            <div class="flex justify-center items-center">{{ chess_mock[26] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is27, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color27()">
            <div class="flex justify-center items-center">{{ chess_mock[27] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is28, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color28()">
            <div class="flex justify-center items-center">{{ chess_mock[28] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': is29, 'chessbtn-green': isgreen }"
            v-on:click="color29()">
            <div class="flex justify-center items-center">{{ chess_mock[29] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is30, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color30()">
            <div class="flex justify-center items-center">{{ chess_mock[30] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is31, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color31()">
            <div class="flex justify-center items-center">{{ chess_mock[31] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is32, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color32()">
            <div class="flex justify-center items-center">{{ chess_mock[32] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is33, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color33()">
            <div class="flex justify-center items-center">{{ chess_mock[33] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is34, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color34()">
            <div class="flex justify-center items-center">{{ chess_mock[34] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is35, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color35()">
            <div class="flex justify-center items-center">{{ chess_mock[35] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is36, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color36()">
            <div class="flex justify-center items-center">{{ chess_mock[36] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is37 }"
            v-on:click="color37()">
            <div class="flex justify-center items-center">{{ chess_mock[37] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is38, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color38()">
            <div class="flex justify-center items-center">{{ chess_mock[38] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is39, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color39()">
            <div class="flex justify-center items-center">{{ chess_mock[39] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is40, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color40()">
            <div class="flex justify-center items-center">{{ chess_mock[40] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is41 }"
            v-on:click="color41()">
            <div class="flex justify-center items-center">{{ chess_mock[41] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is42, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color42()">
            <div class="flex justify-center items-center">{{ chess_mock[42] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is43, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color43()">
            <div class="flex justify-center items-center">{{ chess_mock[43] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is44, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color44()">
            <div class="flex justify-center items-center">{{ chess_mock[44] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is45 }"
            v-on:click="color45()">
            <div class="flex justify-center items-center">{{ chess_mock[45] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is46, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color46()">
            <div class="flex justify-center items-center">{{ chess_mock[46] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is47, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color47()">
            <div class="flex justify-center items-center">{{ chess_mock[47] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is48 }"
            v-on:click="color48()">
            <div class="flex justify-center items-center">{{ chess_mock[48] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is49, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color49()">
            <div class="flex justify-center items-center">{{ chess_mock[49] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is50 }"
            v-on:click="color50()">
            <div class="flex justify-center items-center">{{ chess_mock[50] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is51, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color51()">
            <div class="flex justify-center items-center">{{ chess_mock[51] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is52, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color52()">
            <div class="flex justify-center items-center">{{ chess_mock[52] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is53, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color53()">
            <div class="flex justify-center items-center">{{ chess_mock[53] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is54, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color54()">
            <div class="flex justify-center items-center">{{ chess_mock[54] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is55, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color55()">
            <div class="flex justify-center items-center">{{ chess_mock[55] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is56, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color56()">
            <div class="flex justify-center items-center">{{ chess_mock[56] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is57, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color57()">
            <div class="flex justify-center items-center">{{ chess_mock[57] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': is58, 'chessbtn-green': isgreen }"
            v-on:click="color58()">
            <div class="flex justify-center items-center">{{ chess_mock[58] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is59, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color59()">
            <div class="flex justify-center items-center">{{ chess_mock[59] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is60, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color60()">
            <div class="flex justify-center items-center">{{ chess_mock[60] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is61, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color61()">
            <div class="flex justify-center items-center">{{ chess_mock[61] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue, 'chessbtn-green': is62 }"
            v-on:click="color62()">
            <div class="flex justify-center items-center">{{ chess_mock[62] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is63, 'chessbtn-blue': isblue, 'chessbtn-green': isgreen }"
            v-on:click="color63()">
            <div class="flex justify-center items-center">{{ chess_mock[63] }}</div>
          </td>
        </tr>

      </tbody>
    </table>
    <!-- <table>
      <tr v-for="(row, index) in 8" :key="row">
        <td v-for="(cell, cellIndex) in 8" :key="cell">
          <div class="w-20 h-16 border flex justify-center items-center">
            <div class="flex justify-center items-center"
              v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue }" v-on:click="colorChange()">
              {{ chess_mock[cellIndex + index * 8] }}
            </div>

          </div>
        </td>
      </tr>
    </table> -->



  </div>
</template>

<script>
// import { NsStore } from "../store/index.js";
import { NsStore } from "../../store/index.js";
import { storeToRefs } from "pinia";

export default {
  name: "ChessBoard",
  components: {},
  data() {
    const store = NsStore();
    const { time, NEcounter, BRcounter } = storeToRefs(store);
    return {
      NEcounter, BRcounter,
      isred: false,
      isblue: false,
      isgreen: false,
      is0: false,
      is1: false,
      is2: false,
      is3: false,
      is4: false,
      is5: false,
      is6: false,
      is7: false,
      is8: false, is9: false, is10: false, is11: false, is12: false, is13: false, is14: false, is15: false,
      is16: false, is17: false, is18: false, is19: false, is20: false, is21: false, is22: false, is23: false,
      is24: false, is25: false, is26: false, is27: false, is28: false, is29: false, is30: false, is31: false,
      is32: false, is33: false, is34: false, is35: false, is36: false, is37: false, is38: false, is39: false,
      is40: false, is41: false, is42: false, is43: false, is44: false, is45: false, is46: false, is47: false,
      is48: false, is49: false, is50: false, is51: false, is52: false, is53: false, is54: false, is55: false,
      is56: false, is57: false, is58: false, is59: false, is60: false, is61: false, is62: false, is63: false,

      chess_mock: [[76, 97], [72, 67], [25, 84], [73, 46], [93, 20], [12, 44], [68, 93], [20, 87], [43, 24],
      [68, 44], [62, 97], [72, 66], [96, 16], [42, 3], [14, 44], [51, 37], [63, 40], [76, 86], [43, 66], [13, 63],
      [6, 92], [15, 15], [68, 19], [69, 77], [49, 90], [29, 43], [75, 93], [18, 70], [0, 31], [99, 96], [5, 71], [4, 5],
      [50, 68], [69, 52], [22, 59], [57, 37], [60, 5], [1, 93], [55, 64], [45, 51], [46, 18], [87, 12], [32, 0], [37, 85],
      [43, 3], [70, 93], [53, 62], [26, 18], [80, 8], [85, 13], [54, 80], [37, 43], [23, 11], [91, 48], [85, 57], [53, 25],
      [71, 90], [35, 57], [87, 98], [57, 32], [41, 25], [28, 94], [100, 14], [68, 53]],
    }
  },
  methods: {
    // colorChange: function () {
    //   if (this.chess_mock[(index - 1) * 8 + (cellIndex - 1)][0] > this.chess_mock[(cellIndex - 1) + (index - 1) * 8][1]) {
    //     console.log(this.chess_mock[63][0])
    //     this.isred = true
    //   }
    //   else if (this.chess_mock[(index - 1) * 8 + (cellIndex - 1)][0] > this.chess_mock[(cellIndex - 1) + (index - 1) * 8][1]) {
    //     console.log(this.chess_mock[63][1])
    //     this.isblue = true
    //   }
    // },
    color0: function () {
      this.is0 = true
      this.BRcounter += 1
    },
    color1: function () {
      this.is1 = true
    },
    color2: function () {
      this.is2 = true
    },
    color3: function () {
      this.is3 = true
      this.BRcounter += 1
    },
    color4: function () {
      this.is4 = true
    },
    color5: function () {
      this.is5 = true
    },
    color6: function () {
      this.is6 = true
    },
    color7: function () {
      this.is7 = true
    },
    color8: function () {
      this.is8 = true
    },
    color9: function () {
      this.is9 = true
    },
    color10: function () {
      this.is10 = true
      this.BRcounter += 1
    },
    color11: function () {
      this.is11 = true
    },
    color12: function () {
      this.is12 = true
      this.BRcounter += 1
    },
    color13: function () {
      this.is13 = true
    },
    color14: function () {
      this.is14 = true
    },
    color15: function () {
      this.is15 = true
    },
    color16: function () {
      this.is16 = true
    },
    color17: function () {
      this.is17 = true
    },
    color18: function () {
      this.is18 = true
    },
    color19: function () {
      this.is19 = true
    },
    color20: function () {
      this.is20 = true
      this.BRcounter += 1
    },
    color21: function () {
      this.is21 = true
    },
    color22: function () {
      this.is22 = true
    },
    color23: function () {
      this.is23 = true
      this.BRcounter += 1
    },
    color24: function () {
      this.is24 = true
    },
    color25: function () {
      this.is25 = true
    },
    color26: function () {
      this.is26 = true
    },
    color27: function () {
      this.is27 = true
    },
    color28: function () {
      this.is28 = true
    },
    color29: function () {
      this.is29 = true
      this.NEcounter += 1
    },
    color30: function () {
      this.is30 = true
    },
    color31: function () {
      this.is31 = true
    },
    color32: function () {
      this.is32 = true
    },
    color33: function () {
      this.is33 = true
    },
    color34: function () {
      this.is34 = true
    },
    color35: function () {
      this.is35 = true
    },
    color36: function () {
      this.is36 = true
    },
    color37: function () {
      this.is37 = true
      this.BRcounter += 1
    },
    color38: function () {
      this.is38 = true

    },
    color39: function () {
      this.is39 = true
    },
    color40: function () {
      this.is40 = true
    },
    color41: function () {
      this.is41 = true
      this.BRcounter += 1
    },
    color42: function () {
      this.is42 = true
    },
    color43: function () {
      this.is43 = true

    },
    color44: function () {
      this.is44 = true
    },
    color45: function () {
      this.is45 = true
      this.BRcounter += 1
    },
    color46: function () {
      this.is46 = true
    },
    color47: function () {
      this.is47 = true
    },
    color48: function () {
      this.is48 = true
      this.BRcounter += 1
    },
    color49: function () {
      this.is49 = true
    },
    color50: function () {
      this.is50 = true
      this.BRcounter += 1
    },
    color51: function () {
      this.is51 = true
    },
    color52: function () {
      this.is52 = true
    },
    color53: function () {
      this.is53 = true
    },
    color54: function () {
      this.is54 = true
    },
    color55: function () {
      this.is55 = true
    },
    color56: function () {
      this.is56 = true
    },
    color57: function () {
      this.is57 = true
    },
    color58: function () {
      this.is58 = true
      this.NEcounter += 1
    },
    color59: function () {
      this.is59 = true
    },
    color60: function () {
      this.is60 = true
    },
    color61: function () {
      this.is61 = true
    },
    color62: function () {
      this.is62 = true
      this.BRcounter += 1
    },
    color63: function () {
      this.is63 = true
    },
  },
  mounted() { },
}
</script>

<style scoped>
.chessbtn-blue {
  background-color: blue;
}

.chessbtn-red {
  background-color: red;
}

.chessbtn-green {
  background-color: green;
}
</style>