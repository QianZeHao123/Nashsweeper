<!-- w-20 h-16 -->
<template>
  <div class="flex justify-center items-center h-full w-full align-middle">
    <table class="border-separate border h-full p-4">
      <tbody class="h-full">
        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is0[0], 'chessbtn-blue': is0[1], 'chessbtn-green': is0[2] }"
            v-on:click="color0()">
            <div class="flex justify-center items-center">{{ chess_mock[0] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is1[0], 'chessbtn-blue': is1[1], 'chessbtn-green': is1[2] }"
            v-on:click="color1()">
            <div class="flex justify-center items-center">{{ chess_mock[1] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is2[0], 'chessbtn-blue': is2[1], 'chessbtn-green': is2[2] }"
            v-on:click="color2()">
            <div class="flex justify-center items-center">{{ chess_mock[2] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is3[0], 'chessbtn-blue': is3[1], 'chessbtn-green': is3[2] }"
            v-on:click="color3()">
            <div class="flex justify-center items-center">{{ chess_mock[3] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is4[0], 'chessbtn-blue': is4[1], 'chessbtn-green': is4[2] }"
            v-on:click="color4()">
            <div class="flex justify-center items-center">{{ chess_mock[4] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is5[0], 'chessbtn-blue': is5[1], 'chessbtn-green': is5[2] }"
            v-on:click="color5()">
            <div class="flex justify-center items-center">{{ chess_mock[5] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is6[0], 'chessbtn-blue': is6[1], 'chessbtn-green': is6[2] }"
            v-on:click="color6()">
            <div class="flex justify-center items-center">{{ chess_mock[6] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is7[0], 'chessbtn-blue': is7[1], 'chessbtn-green': is7[2] }"
            v-on:click="color7()">
            <div class="flex justify-center items-center">{{ chess_mock[7] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is8[0], 'chessbtn-blue': is8[1], 'chessbtn-green': is8[2] }"
            v-on:click="color8()">
            <div class="flex justify-center items-center">{{ chess_mock[8] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is9[0], 'chessbtn-blue': is9[1], 'chessbtn-green': is9[2] }"
            v-on:click="color9()">
            <div class="flex justify-center items-center">{{ chess_mock[9] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is10[0], 'chessbtn-blue': is10[1], 'chessbtn-green': is10[2] }"
            v-on:click="color10()">
            <div class="flex justify-center items-center">{{ chess_mock[10] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is11[0], 'chessbtn-blue': is11[1], 'chessbtn-green': is11[2] }"
            v-on:click="color11()">
            <div class="flex justify-center items-center">{{ chess_mock[11] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is12[0], 'chessbtn-blue': is12[1], 'chessbtn-green': is12[2] }"
            v-on:click="color12()">
            <div class="flex justify-center items-center">{{ chess_mock[12] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is13[0], 'chessbtn-blue': is13[1], 'chessbtn-green': is13[2] }"
            v-on:click="color13()">
            <div class="flex justify-center items-center">{{ chess_mock[13] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is14[0], 'chessbtn-blue': is14[1], 'chessbtn-green': is14[2] }"
            v-on:click="color14()">
            <div class="flex justify-center items-center">{{ chess_mock[14] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is15[0], 'chessbtn-blue': is15[1], 'chessbtn-green': is15[2] }"
            v-on:click="color15()">
            <div class="flex justify-center items-center">{{ chess_mock[15] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is16[0], 'chessbtn-blue': is16[1], 'chessbtn-green': is16[2] }"
            v-on:click="color16()">
            <div class="flex justify-center items-center">{{ chess_mock[16] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is17[0], 'chessbtn-blue': is17[1], 'chessbtn-green': is17[2] }"
            v-on:click="color17()">
            <div class="flex justify-center items-center">{{ chess_mock[17] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is18[0], 'chessbtn-blue': is18[1], 'chessbtn-green': is18[2] }"
            v-on:click="color18()">
            <div class="flex justify-center items-center">{{ chess_mock[18] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is19[0], 'chessbtn-blue': is19[1], 'chessbtn-green': is19[2] }"
            v-on:click="color19()">
            <div class="flex justify-center items-center">{{ chess_mock[19] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is20[0], 'chessbtn-blue': is20[1], 'chessbtn-green': is20[2] }"
            v-on:click="color20()">
            <div class="flex justify-center items-center">{{ chess_mock[20] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is21[0], 'chessbtn-blue': is21[1], 'chessbtn-green': is21[2] }"
            v-on:click="color21()">
            <div class="flex justify-center items-center">{{ chess_mock[21] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is22[0], 'chessbtn-blue': is22[1], 'chessbtn-green': is22[2] }"
            v-on:click="color22()">
            <div class="flex justify-center items-center">{{ chess_mock[22] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is23[0], 'chessbtn-blue': is23[1], 'chessbtn-green': is23[2] }"
            v-on:click="color23()">
            <div class="flex justify-center items-center">{{ chess_mock[23] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is24[0], 'chessbtn-blue': is24[1], 'chessbtn-green': is24[2] }"
            v-on:click="color24()">
            <div class="flex justify-center items-center">{{ chess_mock[24] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is25[0], 'chessbtn-blue': is25[1], 'chessbtn-green': is25[2] }"
            v-on:click="color25()">
            <div class="flex justify-center items-center">{{ chess_mock[25] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is26[0], 'chessbtn-blue': is26[1], 'chessbtn-green': is26[2] }"
            v-on:click="color26()">
            <div class="flex justify-center items-center">{{ chess_mock[26] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is27[0], 'chessbtn-blue': is27[1], 'chessbtn-green': is27[2] }"
            v-on:click="color27()">
            <div class="flex justify-center items-center">{{ chess_mock[27] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is28[0], 'chessbtn-blue': is28[1], 'chessbtn-green': is28[2] }"
            v-on:click="color28()">
            <div class="flex justify-center items-center">{{ chess_mock[28] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is29[0], 'chessbtn-blue': is29[1], 'chessbtn-green': is29[2] }"
            v-on:click="color29()">
            <div class="flex justify-center items-center">{{ chess_mock[29] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is30[0], 'chessbtn-blue': is30[1], 'chessbtn-green': is30[2] }"
            v-on:click="color30()">
            <div class="flex justify-center items-center">{{ chess_mock[30] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is31[0], 'chessbtn-blue': is31[1], 'chessbtn-green': is31[2] }"
            v-on:click="color31()">
            <div class="flex justify-center items-center">{{ chess_mock[31] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is32[0], 'chessbtn-blue': is32[1], 'chessbtn-green': is32[2] }"
            v-on:click="color32()">
            <div class="flex justify-center items-center">{{ chess_mock[32] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is33[0], 'chessbtn-blue': is33[1], 'chessbtn-green': is33[2] }"
            v-on:click="color33()">
            <div class="flex justify-center items-center">{{ chess_mock[33] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is34[0], 'chessbtn-blue': is34[1], 'chessbtn-green': is34[2] }"
            v-on:click="color34()">
            <div class="flex justify-center items-center">{{ chess_mock[34] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is35[0], 'chessbtn-blue': is35[1], 'chessbtn-green': is35[2] }"
            v-on:click="color35()">
            <div class="flex justify-center items-center">{{ chess_mock[35] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is36[0], 'chessbtn-blue': is36[1], 'chessbtn-green': is36[2] }"
            v-on:click="color36()">
            <div class="flex justify-center items-center">{{ chess_mock[36] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is37[0], 'chessbtn-blue': is37[1], 'chessbtn-green': is37[2] }"
            v-on:click="color37()">
            <div class="flex justify-center items-center">{{ chess_mock[37] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is38[0], 'chessbtn-blue': is38[1], 'chessbtn-green': is38[2] }"
            v-on:click="color38()">
            <div class="flex justify-center items-center">{{ chess_mock[38] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is39[0], 'chessbtn-blue': is39[1], 'chessbtn-green': is39[2] }"
            v-on:click="color39()">
            <div class="flex justify-center items-center">{{ chess_mock[39] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is40[0], 'chessbtn-blue': is40[1], 'chessbtn-green': is40[2] }"
            v-on:click="color40()">
            <div class="flex justify-center items-center">{{ chess_mock[40] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is41[0], 'chessbtn-blue': is41[1], 'chessbtn-green': is41[2] }"
            v-on:click="color41()">
            <div class="flex justify-center items-center">{{ chess_mock[41] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is42[0], 'chessbtn-blue': is42[1], 'chessbtn-green': is42[2] }"
            v-on:click="color42()">
            <div class="flex justify-center items-center">{{ chess_mock[42] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is43[0], 'chessbtn-blue': is43[1], 'chessbtn-green': is43[2] }"
            v-on:click="color43()">
            <div class="flex justify-center items-center">{{ chess_mock[43] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is44[0], 'chessbtn-blue': is44[1], 'chessbtn-green': is44[2] }"
            v-on:click="color44()">
            <div class="flex justify-center items-center">{{ chess_mock[44] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is45[0], 'chessbtn-blue': is45[1], 'chessbtn-green': is45[2] }"
            v-on:click="color45()">
            <div class="flex justify-center items-center">{{ chess_mock[45] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is46[0], 'chessbtn-blue': is46[1], 'chessbtn-green': is46[2] }"
            v-on:click="color46()">
            <div class="flex justify-center items-center">{{ chess_mock[46] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is47[0], 'chessbtn-blue': is47[1], 'chessbtn-green': is47[2] }"
            v-on:click="color47()">
            <div class="flex justify-center items-center">{{ chess_mock[47] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is48[0], 'chessbtn-blue': is48[1], 'chessbtn-green': is48[2] }"
            v-on:click="color48()">
            <div class="flex justify-center items-center">{{ chess_mock[48] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is49[0], 'chessbtn-blue': is49[1], 'chessbtn-green': is49[2] }"
            v-on:click="color49()">
            <div class="flex justify-center items-center">{{ chess_mock[49] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is50[0], 'chessbtn-blue': is50[1], 'chessbtn-green': is50[2] }"
            v-on:click="color50()">
            <div class="flex justify-center items-center">{{ chess_mock[50] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is51[0], 'chessbtn-blue': is51[1], 'chessbtn-green': is51[2] }"
            v-on:click="color51()">
            <div class="flex justify-center items-center">{{ chess_mock[51] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is52[0], 'chessbtn-blue': is52[1], 'chessbtn-green': is52[2] }"
            v-on:click="color52()">
            <div class="flex justify-center items-center">{{ chess_mock[52] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is53[0], 'chessbtn-blue': is53[1], 'chessbtn-green': is53[2] }"
            v-on:click="color53()">
            <div class="flex justify-center items-center">{{ chess_mock[53] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is54[0], 'chessbtn-blue': is54[1], 'chessbtn-green': is54[2] }"
            v-on:click="color54()">
            <div class="flex justify-center items-center">{{ chess_mock[54] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is55[0], 'chessbtn-blue': is55[1], 'chessbtn-green': is55[2] }"
            v-on:click="color55()">
            <div class="flex justify-center items-center">{{ chess_mock[55] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is56[0], 'chessbtn-blue': is56[1], 'chessbtn-green': is56[2] }"
            v-on:click="color56()">
            <div class="flex justify-center items-center">{{ chess_mock[56] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is57[0], 'chessbtn-blue': is57[1], 'chessbtn-green': is57[2] }"
            v-on:click="color57()">
            <div class="flex justify-center items-center">{{ chess_mock[57] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is58[0], 'chessbtn-blue': is58[1], 'chessbtn-green': is58[2] }"
            v-on:click="color58()">
            <div class="flex justify-center items-center">{{ chess_mock[58] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is59[0], 'chessbtn-blue': is59[1], 'chessbtn-green': is59[2] }"
            v-on:click="color59()">
            <div class="flex justify-center items-center">{{ chess_mock[59] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is60[0], 'chessbtn-blue': is60[1], 'chessbtn-green': is60[2] }"
            v-on:click="color60()">
            <div class="flex justify-center items-center">{{ chess_mock[60] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is61[0], 'chessbtn-blue': is61[1], 'chessbtn-green': is61[2] }"
            v-on:click="color61()">
            <div class="flex justify-center items-center">{{ chess_mock[61] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is62[0], 'chessbtn-blue': is62[1], 'chessbtn-green': is62[2] }"
            v-on:click="color62()">
            <div class="flex justify-center items-center">{{ chess_mock[62] }}</div>
          </td>
          <td class="w-20 h-16 border"
            v-bind:class="{ 'chessbtn-red': is63[0], 'chessbtn-blue': is63[1], 'chessbtn-green': is63[2] }"
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
                v-bind:class="{ 'chessbtn-red': is1[0], 'chessbtn-blue': is1[0] }" v-on:click="colorChange()">
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
  name: "PadChessBoard",
  components: {},
  data() {
    const store = NsStore();
    const { NEcounter, BRcounter, time } = storeToRefs(store);
    const gameOverStr = '';
    return {
      NEcounter, BRcounter, gameOverStr, time,
      is0: [false, false, false], is1: [false, false, false], is2: [false, false, false], is3: [false, false, false], is4: [false, false, false], is5: [false, false, false], is6: [false, false, false], is7: [false, false, false],
      is8: [false, false, false], is9: [false, false, false], is10: [false, false, false], is11: [false, false, false], is12: [false, false, false], is13: [false, false, false], is14: [false, false, false], is15: [false, false, false],
      is16: [false, false, false], is17: [false, false, false], is18: [false, false, false], is19: [false, false, false], is20: [false, false, false], is21: [false, false, false], is22: [false, false, false], is23: [false, false, false],
      is24: [false, false, false], is25: [false, false, false], is26: [false, false, false], is27: [false, false, false], is28: [false, false, false], is29: [false, false, false], is30: [false, false, false], is31: [false, false, false],
      is32: [false, false, false], is33: [false, false, false], is34: [false, false, false], is35: [false, false, false], is36: [false, false, false], is37: [false, false, false], is38: [false, false, false], is39: [false, false, false],
      is40: [false, false, false], is41: [false, false, false], is42: [false, false, false], is43: [false, false, false], is44: [false, false, false], is45: [false, false, false], is46: [false, false, false], is47: [false, false, false],
      is48: [false, false, false], is49: [false, false, false], is50: [false, false, false], is51: [false, false, false], is52: [false, false, false], is53: [false, false, false], is54: [false, false, false], is55: [false, false, false],
      is56: [false, false, false], is57: [false, false, false], is58: [false, false, false], is59: [false, false, false], is60: [false, false, false], is61: [false, false, false], is62: [false, false, false], is63: [false, false, false],

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
    //     this.is1[0] = true
    //   }
    //   else if (this.chess_mock[(index - 1) * 8 + (cellIndex - 1)][0] > this.chess_mock[(cellIndex - 1) + (index - 1) * 8][1]) {
    //     console.log(this.chess_mock[63][1])
    //     this.is1[0] = true
    //   }
    // },
    color0: function () {
      this.is0 = [false, false, true]
      this.is1 = [true, false, false]
      this.is2 = [true, false, false]
      this.is3 = [true, false, false]
      this.is4 = [true, false, false]
      this.is5 = [true, false, false]
      this.is6 = [true, false, false]
      this.is7 = [true, false, false]
      this.BRcounter += 1
    },
    color1: function () {
      this.is1 = [true, false, false]
    },
    color2: function () {
      this.is2 = [true, false, false]
    },
    color3: function () {
      this.is3 = [false, false, true]
      this.is11 = [true, false, false]
      this.is19 = [true, false, false]
      this.is27 = [true, false, false]
      this.is35 = [true, false, false]
      this.is43 = [true, false, false]
      this.is51 = [true, false, false]
      this.is59 = [true, false, false]
      this.BRcounter += 1
    },
    color4: function () {
      this.is4 = [true, false, false]
    },
    color5: function () {
      this.is5 = [true, false, false]
    },
    color6: function () {
      this.is6 = [true, false, false]
    },
    color7: function () {
      this.is7 = [true, false, false]
    },
    color8: function () {
      this.is8 = [true, false, false]
    },
    color9: function () {
      this.is9 = [true, false, false]
    },
    color10: function () {
      this.is8 = [true, false, false]
      this.is9 = [true, false, false]
      this.is10 = [false, false, true]
      this.is11 = [true, false, false]
      this.is12 = [true, false, false]
      this.is13 = [true, false, false]
      this.is14 = [true, false, false]
      this.is15 = [true, false, false]
      this.BRcounter += 1
    },
    color11: function () {
      this.is11 = [true, false, false]
    },
    color12: function () {
      this.is4 = [true, false, false]
      this.is12 = [false, false, true]
      this.is20 = [true, false, false]
      this.is28 = [true, false, false]
      this.is36 = [true, false, false]
      this.is44 = [true, false, false]
      this.is52 = [true, false, false]
      this.is60 = [true, false, false]
      this.BRcounter += 1
    },
    color13: function () {
      this.is13 = [true, false, false]

    },
    color14: function () {
      this.is14 = [true, false, false]
    },
    color15: function () {
      this.is15 = [true, false, false]
    },
    color16: function () {
      this.is16 = [true, false, false]
    },
    color17: function () {
      this.is17 = [true, false, false]
    },
    color18: function () {
      this.is18 = [true, false, false]
    },
    color19: function () {
      this.is19 = [true, false, false]
    },
    color20: function () {
      this.is16 = [true, false, false]
      this.is17 = [true, false, false]
      this.is18 = [true, false, false]
      this.is19 = [true, false, false]
      this.is20 = [false, false, true]
      this.is21 = [true, false, false]
      this.is22 = [true, false, false]
      this.is23 = [true, false, false]
      this.BRcounter += 1
    },
    color21: function () {
      this.is21 = [true, false, false]
    },
    color22: function () {
      this.is22 = [true, false, false]
    },
    color23: function () {
      this.is7 = [true, false, false]
      this.is15 = [true, false, false]
      this.is23 = [false, false, true]
      this.is31 = [true, false, false]
      this.is39 = [true, false, false]
      this.is47 = [true, false, false]
      this.is55 = [true, false, false]
      this.is63 = [true, false, false]
      this.BRcounter += 1
    },
    color24: function () {
      this.is24 = [true, false, false]
    },
    color25: function () {
      this.is25 = [true, false, false]
    },
    color26: function () {
      this.is26 = [true, false, false]
    },
    color27: function () {
      this.is27 = [true, false, false]
    },
    color28: function () {
      this.is28 = [true, false, false]
    },
    color29: function () {
      this.is24 = [true, false, false]
      this.is25 = [true, false, false]
      this.is26 = [true, false, false]
      this.is27 = [true, false, false]
      this.is28 = [true, false, false]
      this.is29 = [false, true, false]
      this.is30 = [true, false, false]
      this.is31 = [true, false, false]
      this.is5 = [true, false, false]
      this.is13 = [true, false, false]
      this.is21 = [true, false, false]
      this.is61 = [true, false, false]
      this.is37 = [true, false, false]
      this.is45 = [true, false, false]
      this.is53 = [true, false, false]
      this.NEcounter += 1
    },
    color30: function () {
      this.is30 = [true, false, false]
    },
    color31: function () {
      this.is31 = [true, false, false]
    },
    color32: function () {
      this.is32 = [true, false, false]
    },
    color33: function () {
      this.is33 = [true, false, false]
    },
    color34: function () {
      this.is34 = [true, false, false]
    },
    color35: function () {
      this.is35 = [true, false, false]
    },
    color36: function () {
      this.is36 = [true, false, false]
    },
    color37: function () {
      this.is32 = [true, false, false]
      this.is33 = [true, false, false]
      this.is34 = [true, false, false]
      this.is35 = [true, false, false]
      this.is36 = [true, false, false]
      this.is37 = [false, false, true]
      this.is38 = [true, false, false]
      this.is39 = [true, false, false]
      this.BRcounter += 1
    },
    color38: function () {
      this.is38 = [true, false, false]

    },
    color39: function () {
      this.is39 = [true, false, false]
    },
    color40: function () {
      this.is40 = [true, false, false]
    },
    color41: function () {
      this.is1 = [true, false, false]
      this.is9 = [true, false, false]
      this.is17 = [true, false, false]
      this.is25 = [true, false, false]
      this.is33 = [true, false, false]
      this.is41 = [false, false, true]
      this.is49 = [true, false, false]
      this.is57 = [true, false, false]
      this.BRcounter += 1
    },
    color42: function () {
      this.is42 = [true, false, false]
    },
    color43: function () {
      this.is43 = [true, false, false]
    },
    color44: function () {
      this.is44 = [true, false, false]
    },
    color45: function () {
      this.is40 = [true, false, false]
      this.is41 = [true, false, false]
      this.is42 = [true, false, false]
      this.is43 = [true, false, false]
      this.is44 = [true, false, false]
      this.is45 = [false, false, true]
      this.is46 = [true, false, false]
      this.is47 = [true, false, false]
      this.BRcounter += 1
    },
    color46: function () {
      this.is46 = [true, false, false]
    },
    color47: function () {
      this.is47 = [true, false, false]
    },
    color48: function () {
      this.is0 = [true, false, false]
      this.is8 = [true, false, false]
      this.is16 = [true, false, false]
      this.is24 = [true, false, false]
      this.is32 = [true, false, false]
      this.is40 = [true, false, false]
      this.is48 = [false, false, true]
      this.is56 = [true, false, false]
      this.BRcounter += 1
    },
    color49: function () {
      this.is49 = [true, false, false]
    },
    color50: function () {
      this.is48 = [true, false, false]
      this.is49 = [true, false, false]
      this.is50 = [false, false, true]
      this.is51 = [true, false, false]
      this.is52 = [true, false, false]
      this.is53 = [true, false, false]
      this.is54 = [true, false, false]
      this.is55 = [true, false, false]
      this.BRcounter += 1
    },
    color51: function () {
      this.is51 = [true, false, false]
    },
    color52: function () {
      this.is52 = [true, false, false]
    },
    color53: function () {
      this.is53 = [true, false, false]
    },
    color54: function () {
      this.is54 = [true, false, false]
    },
    color55: function () {
      this.is55 = [true, false, false]
    },
    color56: function () {
      this.is56 = [true, false, false]
    },
    color57: function () {
      this.is57 = [true, false, false]
    },
    color58: function () {
      this.is56 = [true, false, false]
      this.is57 = [true, false, false]
      this.is58 = [false, true, false]
      this.is59 = [true, false, false]
      this.is60 = [true, false, false]
      this.is61 = [true, false, false]
      this.is62 = [true, false, false]
      this.is63 = [true, false, false]
      this.is2 = [true, false, false]
      this.is10 = [true, false, false]
      this.is18 = [true, false, false]
      this.is26 = [true, false, false]
      this.is34 = [true, false, false]
      this.is42 = [true, false, false]
      this.is50 = [true, false, false]
      this.NEcounter += 1
    },
    color59: function () {
      this.is59 = [true, false, false]
    },
    color60: function () {
      this.is60 = [true, false, false]
    },
    color61: function () {
      this.is61 = [true, false, false]
    },
    color62: function () {
      this.is6 = [true, false, false]
      this.is14 = [true, false, false]
      this.is22 = [true, false, false]
      this.is30 = [true, false, false]
      this.is38 = [true, false, false]
      this.is46 = [true, false, false]
      this.is54 = [true, false, false]
      this.is62 = [false, false, true]
      this.BRcounter += 1
    },
    color63: function () {
      this.is63 = [true, false, false]
    },
    GameOver: function () {
      if (this.NEcounter == 2) {
        this.gameOverStr = "Game Over, you have found all the Nash Equilibrium and " + this.BRcounter + " Best Response, " + "You spent a total of " + +this.time.hour + ":" + this.time.minute + ":" + this.time.second;
        alert(this.gameOverStr);
      }
    },
  },
  mounted() {
    // execute every 1 s
    this.timer = setInterval(() => {
      this.GameOver()
    }, 1000);

  },
}
</script>
  




<style scoped>
.chessbtn-blue {
  background-color: #3b82f6;
}

.chessbtn-red {
  background-color: #eea4a4;
}

.chessbtn-green {
  background-color: #22c55e;
}
</style>