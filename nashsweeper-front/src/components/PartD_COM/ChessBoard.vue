<template>
    <div class="flex justify-center items-center h-full w-full align-middle">
        <!-- CheckerBoard -->
        <table class="border-separate border w-full h-full p-4">
            <tbody class="h-full w-full">
                <!-- Row 0 -->
                <tr>
                    <!-- Row 0  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[0][0], 'chessbtn-blue': cc[0][1], 'chessbtn-green': cc[0][2] }">
                        <div class="flex justify-center items-center">{{ cm[0] }}</div>
                    </td>
                    <!-- Row 0  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[1][0], 'chessbtn-blue': cc[1][1], 'chessbtn-green': cc[1][2] }">
                        <div class="flex justify-center items-center">{{ cm[1] }}</div>
                    </td>
                    <!-- Row 0  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[2][0], 'chessbtn-blue': cc[2][1], 'chessbtn-green': cc[2][2] }">
                        <div class="flex justify-center items-center">{{ cm[2] }}</div>
                    </td>
                    <!-- Row 0  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[3][0], 'chessbtn-blue': cc[3][1], 'chessbtn-green': cc[3][2] }">
                        <div class="flex justify-center items-center">{{ cm[3] }}</div>
                    </td>
                    <!-- Row 0  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[4][0], 'chessbtn-blue': cc[4][1], 'chessbtn-green': cc[4][2] }">
                        <div class="flex justify-center items-center">{{ cm[4] }}</div>
                    </td>
                    <!-- Row 0  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[5][0], 'chessbtn-blue': cc[5][1], 'chessbtn-green': cc[5][2] }">
                        <div class="flex justify-center items-center">{{ cm[5] }}</div>
                    </td>
                    <!-- Row 0  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[6][0], 'chessbtn-blue': cc[6][1], 'chessbtn-green': cc[6][2] }">
                        <div class="flex justify-center items-center">{{ cm[6] }}</div>
                    </td>
                    <!-- Row 0  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[7][0], 'chessbtn-blue': cc[7][1], 'chessbtn-green': cc[7][2] }">
                        <div class="flex justify-center items-center">{{ cm[7] }}</div>
                    </td>
                </tr>
                <!-- Row 1 -->
                <tr>
                    <!-- Row 1  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[8][0], 'chessbtn-blue': cc[8][1], 'chessbtn-green': cc[8][2] }">
                        <div class="flex justify-center items-center">{{ cm[8] }}</div>
                    </td>
                    <!-- Row 1  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[9][0], 'chessbtn-blue': cc[9][1], 'chessbtn-green': cc[9][2] }">
                        <div class="flex justify-center items-center">{{ cm[9] }}</div>
                    </td>
                    <!-- Row 1  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[10][0], 'chessbtn-blue': cc[10][1], 'chessbtn-green': cc[10][2] }">
                        <div class="flex justify-center items-center">{{ cm[10] }}</div>
                    </td>
                    <!-- Row 1  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[11][0], 'chessbtn-blue': cc[11][1], 'chessbtn-green': cc[11][2] }">
                        <div class="flex justify-center items-center">{{ cm[11] }}</div>
                    </td>
                    <!-- Row 1  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[12][0], 'chessbtn-blue': cc[12][1], 'chessbtn-green': cc[12][2] }">
                        <div class="flex justify-center items-center">{{ cm[12] }}</div>
                    </td>
                    <!-- Row 1  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[13][0], 'chessbtn-blue': cc[13][1], 'chessbtn-green': cc[13][2] }">
                        <div class="flex justify-center items-center">{{ cm[13] }}</div>
                    </td>
                    <!-- Row 1  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[14][0], 'chessbtn-blue': cc[14][1], 'chessbtn-green': cc[14][2] }">
                        <div class="flex justify-center items-center">{{ cm[14] }}</div>
                    </td>
                    <!-- Row 1  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[15][0], 'chessbtn-blue': cc[15][1], 'chessbtn-green': cc[15][2] }">
                        <div class="flex justify-center items-center">{{ cm[15] }}</div>
                    </td>
                </tr>
                <!-- Row 2 -->
                <tr>
                    <!-- Row 2  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[16][0], 'chessbtn-blue': cc[16][1], 'chessbtn-green': cc[16][2] }">
                        <div class="flex justify-center items-center">{{ cm[16] }}</div>
                    </td>
                    <!-- Row 2  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[17][0], 'chessbtn-blue': cc[17][1], 'chessbtn-green': cc[17][2] }">
                        <div class="flex justify-center items-center">{{ cm[17] }}</div>
                    </td>
                    <!-- Row 2  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[18][0], 'chessbtn-blue': cc[18][1], 'chessbtn-green': cc[18][2] }">
                        <div class="flex justify-center items-center">{{ cm[18] }}</div>
                    </td>
                    <!-- Row 2  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[19][0], 'chessbtn-blue': cc[19][1], 'chessbtn-green': cc[19][2] }">
                        <div class="flex justify-center items-center">{{ cm[19] }}</div>
                    </td>
                    <!-- Row 2  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[20][0], 'chessbtn-blue': cc[20][1], 'chessbtn-green': cc[20][2] }">
                        <div class="flex justify-center items-center">{{ cm[20] }}</div>
                    </td>
                    <!-- Row 2  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[21][0], 'chessbtn-blue': cc[21][1], 'chessbtn-green': cc[21][2] }">
                        <div class="flex justify-center items-center">{{ cm[21] }}</div>
                    </td>
                    <!-- Row 2  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[22][0], 'chessbtn-blue': cc[22][1], 'chessbtn-green': cc[22][2] }">
                        <div class="flex justify-center items-center">{{ cm[22] }}</div>
                    </td>
                    <!-- Row 2  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[23][0], 'chessbtn-blue': cc[23][1], 'chessbtn-green': cc[23][2] }">
                        <div class="flex justify-center items-center">{{ cm[23] }}</div>
                    </td>
                </tr>
                <!-- Row 3 -->
                <tr>
                    <!-- Row 3  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[24][0], 'chessbtn-blue': cc[24][1], 'chessbtn-green': cc[24][2] }">
                        <div class="flex justify-center items-center">{{ cm[24] }}</div>
                    </td>
                    <!-- Row 3  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[25][0], 'chessbtn-blue': cc[25][1], 'chessbtn-green': cc[25][2] }">
                        <div class="flex justify-center items-center">{{ cm[25] }}</div>
                    </td>
                    <!-- Row 3  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[26][0], 'chessbtn-blue': cc[26][1], 'chessbtn-green': cc[26][2] }">
                        <div class="flex justify-center items-center">{{ cm[26] }}</div>
                    </td>
                    <!-- Row 3  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[27][0], 'chessbtn-blue': cc[27][1], 'chessbtn-green': cc[27][2] }">
                        <div class="flex justify-center items-center">{{ cm[27] }}</div>
                    </td>
                    <!-- Row 3  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[28][0], 'chessbtn-blue': cc[28][1], 'chessbtn-green': cc[28][2] }">
                        <div class="flex justify-center items-center">{{ cm[28] }}</div>
                    </td>
                    <!-- Row 3  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[29][0], 'chessbtn-blue': cc[29][1], 'chessbtn-green': cc[29][2] }">
                        <div class="flex justify-center items-center">{{ cm[29] }}</div>
                    </td>
                    <!-- Row 3  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[30][0], 'chessbtn-blue': cc[30][1], 'chessbtn-green': cc[30][2] }">
                        <div class="flex justify-center items-center">{{ cm[30] }}</div>
                    </td>
                    <!-- Row 3  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[31][0], 'chessbtn-blue': cc[31][1], 'chessbtn-green': cc[31][2] }">
                        <div class="flex justify-center items-center">{{ cm[31] }}</div>
                    </td>
                </tr>
                <!-- Row 4 -->
                <!-- Row 5 -->
                <!-- Row 6 -->
                <!-- Row 7 -->
            </tbody>
        </table>
    </div>
</template>

<script>
import { CellColorDataInit } from './CheckerboardCom/CellColor.js';
import { ChessMock } from './CheckerboardCom/testGame.js';
export default {
    name: "ChessBoard",
    components: {},
    data() {
        const cc = CellColorDataInit;
        const cm = ChessMock;
        // cc[x][0] Red, cc[x][1] Blue, cc[x][2] Green
        // cc[0][1] = true
        return {
            cc, cm
        }
    },
    methods: {
        testClick: function () {
            console.log(this.cm[0][0])
        }
    },
    mounted() { },
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