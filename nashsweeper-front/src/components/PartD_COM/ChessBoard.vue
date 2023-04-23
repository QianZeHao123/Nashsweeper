<template>
  <div>
    <!-- <table class="border-separate border ">
      <tbody>
        <tr>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[0] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[1] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[2] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[3] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[4] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[5] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[6] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[7] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[8] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[9] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[10] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[11] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[12] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[13] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[14] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[15] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[16] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[17] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[18] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[19] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[20] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[21] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[22] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[23] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[24] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[25] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[26] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[27] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[28] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[29] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[30] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[31] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[32] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[33] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[34] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[35] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[36] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[37] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[38] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[39] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[40] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[41] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[42] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[43] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[44] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[45] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[46] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[47] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[48] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[49] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[50] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[51] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[52] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[53] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[54] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[55] }}</div>
          </td>
        </tr>

        <tr>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[56] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[57] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[58] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[59] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[60] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[61] }}</div>
          </td>
          <td class="w-20 h-16 border">
            <div class="flex justify-center items-center">{{ chess_mock[62] }}</div>
          </td>
          <td class="w-20 h-16 border" v-bind:class="{ 'chessbtn-red': isred, 'chessbtn-blue': isblue }"
            v-on:click="colorChange()">
            <div class="flex justify-center items-center">{{ chess_mock[63] }}</div>
          </td>
        </tr>

      </tbody>
    </table> -->
    <table>
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
    </table>



  </div>
</template>

<script>
export default {
  name: "ChessBoard",
  components: {},
  data() {
    return {
      isred: false,
      isblue: false,
      chess_mock: [[45, 87], [50, 65], [57, 20], [75, 1], [39, 21], [90, 43], [19, 85], [53, 82], [55, 83],
      [13, 45], [39, 1], [11, 16], [50, 33], [94, 36], [29, 73], [39, 91], [77, 49], [93, 43], [16, 67], [41, 47],
      [57, 35], [6, 17], [52, 57], [80, 13], [55, 89], [60, 94], [58, 39], [43, 47], [50, 91], [1, 92], [54, 79], [21, 92],
      [4, 44], [38, 15], [37, 54], [93, 62], [28, 35], [23, 76], [88, 91], [27, 55], [37, 56], [76, 57], [33, 17], [73, 16],
      [43, 59], [84, 28], [70, 12], [33, 16], [28, 36], [83, 47], [79, 70], [65, 94], [57, 66], [21, 90], [62, 12], [88, 17],
      [94, 2], [93, 34], [66, 93], [97, 87], [71, 93], [96, 84], [71, 97], [55, 84]],
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
</style>