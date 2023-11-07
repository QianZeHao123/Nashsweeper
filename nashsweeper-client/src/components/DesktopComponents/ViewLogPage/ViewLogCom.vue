<template>
    <div class="flex justify-center items-center h-full w-full align-middle">
        <!-- CheckerBoard -->
        <table class="border-separate border w-full h-full p-4">
            <tbody class="h-full w-full">
                <!-- Row 0 -->
                <tr>
                    <!-- Row 0  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[0][0], 'chessbtn-blue': cc[0][1], 'chessbtn-green': cc[0][2] }"
                        v-on:click="ClickCell0()">
                        <div class="flex justify-center items-center">{{ cm[0] }}</div>
                    </td>
                    <!-- Row 0  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[1][0], 'chessbtn-blue': cc[1][1], 'chessbtn-green': cc[1][2] }"
                        v-on:click="ClickCell1()">
                        <div class="flex justify-center items-center">{{ cm[1] }}</div>
                    </td>
                    <!-- Row 0  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[2][0], 'chessbtn-blue': cc[2][1], 'chessbtn-green': cc[2][2] }"
                        v-on:click="ClickCell2()">
                        <div class="flex justify-center items-center">{{ cm[2] }}</div>
                    </td>
                    <!-- Row 0  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[3][0], 'chessbtn-blue': cc[3][1], 'chessbtn-green': cc[3][2] }"
                        v-on:click="ClickCell3()">
                        <div class="flex justify-center items-center">{{ cm[3] }}</div>
                    </td>
                    <!-- Row 0  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[4][0], 'chessbtn-blue': cc[4][1], 'chessbtn-green': cc[4][2] }"
                        v-on:click="ClickCell4()">
                        <div class="flex justify-center items-center">{{ cm[4] }}</div>
                    </td>
                    <!-- Row 0  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[5][0], 'chessbtn-blue': cc[5][1], 'chessbtn-green': cc[5][2] }"
                        v-on:click="ClickCell5()">
                        <div class="flex justify-center items-center">{{ cm[5] }}</div>
                    </td>
                    <!-- Row 0  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[6][0], 'chessbtn-blue': cc[6][1], 'chessbtn-green': cc[6][2] }"
                        v-on:click="ClickCell6()">
                        <div class="flex justify-center items-center">{{ cm[6] }}</div>
                    </td>
                    <!-- Row 0  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[7][0], 'chessbtn-blue': cc[7][1], 'chessbtn-green': cc[7][2] }"
                        v-on:click="ClickCell7()">
                        <div class="flex justify-center items-center">{{ cm[7] }}</div>
                    </td>
                </tr>
                <!-- Row 1 -->
                <tr>
                    <!-- Row 1  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[8][0], 'chessbtn-blue': cc[8][1], 'chessbtn-green': cc[8][2] }"
                        v-on:click="ClickCell8()">
                        <div class="flex justify-center items-center">{{ cm[8] }}</div>
                    </td>
                    <!-- Row 1  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[9][0], 'chessbtn-blue': cc[9][1], 'chessbtn-green': cc[9][2] }"
                        v-on:click="ClickCell9()">
                        <div class="flex justify-center items-center">{{ cm[9] }}</div>
                    </td>
                    <!-- Row 1  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[10][0], 'chessbtn-blue': cc[10][1], 'chessbtn-green': cc[10][2] }"
                        v-on:click="ClickCell10()">
                        <div class="flex justify-center items-center">{{ cm[10] }}</div>
                    </td>
                    <!-- Row 1  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[11][0], 'chessbtn-blue': cc[11][1], 'chessbtn-green': cc[11][2] }"
                        v-on:click="ClickCell11()">
                        <div class="flex justify-center items-center">{{ cm[11] }}</div>
                    </td>
                    <!-- Row 1  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[12][0], 'chessbtn-blue': cc[12][1], 'chessbtn-green': cc[12][2] }"
                        v-on:click="ClickCell12()">
                        <div class="flex justify-center items-center">{{ cm[12] }}</div>
                    </td>
                    <!-- Row 1  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[13][0], 'chessbtn-blue': cc[13][1], 'chessbtn-green': cc[13][2] }"
                        v-on:click="ClickCell13()">
                        <div class="flex justify-center items-center">{{ cm[13] }}</div>
                    </td>
                    <!-- Row 1  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[14][0], 'chessbtn-blue': cc[14][1], 'chessbtn-green': cc[14][2] }"
                        v-on:click="ClickCell14()">
                        <div class="flex justify-center items-center">{{ cm[14] }}</div>
                    </td>
                    <!-- Row 1  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[15][0], 'chessbtn-blue': cc[15][1], 'chessbtn-green': cc[15][2] }"
                        v-on:click="ClickCell15()">
                        <div class="flex justify-center items-center">{{ cm[15] }}</div>
                    </td>
                </tr>
                <!-- Row 2 -->
                <tr>
                    <!-- Row 2  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[16][0], 'chessbtn-blue': cc[16][1], 'chessbtn-green': cc[16][2] }"
                        v-on:click="ClickCell16()">
                        <div class="flex justify-center items-center">{{ cm[16] }}</div>
                    </td>
                    <!-- Row 2  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[17][0], 'chessbtn-blue': cc[17][1], 'chessbtn-green': cc[17][2] }"
                        v-on:click="ClickCell17()">
                        <div class="flex justify-center items-center">{{ cm[17] }}</div>
                    </td>
                    <!-- Row 2  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[18][0], 'chessbtn-blue': cc[18][1], 'chessbtn-green': cc[18][2] }"
                        v-on:click="ClickCell18()">
                        <div class="flex justify-center items-center">{{ cm[18] }}</div>
                    </td>
                    <!-- Row 2  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[19][0], 'chessbtn-blue': cc[19][1], 'chessbtn-green': cc[19][2] }"
                        v-on:click="ClickCell19()">
                        <div class="flex justify-center items-center">{{ cm[19] }}</div>
                    </td>
                    <!-- Row 2  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[20][0], 'chessbtn-blue': cc[20][1], 'chessbtn-green': cc[20][2] }"
                        v-on:click="ClickCell20()">
                        <div class="flex justify-center items-center">{{ cm[20] }}</div>
                    </td>
                    <!-- Row 2  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[21][0], 'chessbtn-blue': cc[21][1], 'chessbtn-green': cc[21][2] }"
                        v-on:click="ClickCell21()">
                        <div class="flex justify-center items-center">{{ cm[21] }}</div>
                    </td>
                    <!-- Row 2  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[22][0], 'chessbtn-blue': cc[22][1], 'chessbtn-green': cc[22][2] }"
                        v-on:click="ClickCell22()">
                        <div class="flex justify-center items-center">{{ cm[22] }}</div>
                    </td>
                    <!-- Row 2  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[23][0], 'chessbtn-blue': cc[23][1], 'chessbtn-green': cc[23][2] }"
                        v-on:click="ClickCell23()">
                        <div class="flex justify-center items-center">{{ cm[23] }}</div>
                    </td>
                </tr>
                <!-- Row 3 -->
                <tr>
                    <!-- Row 3  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[24][0], 'chessbtn-blue': cc[24][1], 'chessbtn-green': cc[24][2] }"
                        v-on:click="ClickCell24()">
                        <div class="flex justify-center items-center">{{ cm[24] }}</div>
                    </td>
                    <!-- Row 3  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[25][0], 'chessbtn-blue': cc[25][1], 'chessbtn-green': cc[25][2] }"
                        v-on:click="ClickCell25()">
                        <div class="flex justify-center items-center">{{ cm[25] }}</div>
                    </td>
                    <!-- Row 3  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[26][0], 'chessbtn-blue': cc[26][1], 'chessbtn-green': cc[26][2] }"
                        v-on:click="ClickCell26()">
                        <div class="flex justify-center items-center">{{ cm[26] }}</div>
                    </td>
                    <!-- Row 3  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[27][0], 'chessbtn-blue': cc[27][1], 'chessbtn-green': cc[27][2] }"
                        v-on:click="ClickCell27()">
                        <div class="flex justify-center items-center">{{ cm[27] }}</div>
                    </td>
                    <!-- Row 3  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[28][0], 'chessbtn-blue': cc[28][1], 'chessbtn-green': cc[28][2] }"
                        v-on:click="ClickCell28()">
                        <div class="flex justify-center items-center">{{ cm[28] }}</div>
                    </td>
                    <!-- Row 3  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[29][0], 'chessbtn-blue': cc[29][1], 'chessbtn-green': cc[29][2] }"
                        v-on:click="ClickCell29()">
                        <div class="flex justify-center items-center">{{ cm[29] }}</div>
                    </td>
                    <!-- Row 3  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[30][0], 'chessbtn-blue': cc[30][1], 'chessbtn-green': cc[30][2] }"
                        v-on:click="ClickCell30()">
                        <div class="flex justify-center items-center">{{ cm[30] }}</div>
                    </td>
                    <!-- Row 3  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[31][0], 'chessbtn-blue': cc[31][1], 'chessbtn-green': cc[31][2] }"
                        v-on:click="ClickCell31()">
                        <div class="flex justify-center items-center">{{ cm[31] }}</div>
                    </td>
                </tr>
                <!-- Row 4 -->
                <tr>
                    <!-- Row 4  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[32][0], 'chessbtn-blue': cc[32][1], 'chessbtn-green': cc[32][2] }"
                        v-on:click="ClickCell32()">
                        <div class="flex justify-center items-center">{{ cm[32] }}</div>
                    </td>
                    <!-- Row 4  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[33][0], 'chessbtn-blue': cc[33][1], 'chessbtn-green': cc[33][2] }"
                        v-on:click="ClickCell33()">
                        <div class="flex justify-center items-center">{{ cm[33] }}</div>
                    </td>
                    <!-- Row 4  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[34][0], 'chessbtn-blue': cc[34][1], 'chessbtn-green': cc[34][2] }"
                        v-on:click="ClickCell34()">
                        <div class="flex justify-center items-center">{{ cm[34] }}</div>
                    </td>
                    <!-- Row 4  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[35][0], 'chessbtn-blue': cc[35][1], 'chessbtn-green': cc[35][2] }"
                        v-on:click="ClickCell35()">
                        <div class="flex justify-center items-center">{{ cm[35] }}</div>
                    </td>
                    <!-- Row 4  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[36][0], 'chessbtn-blue': cc[36][1], 'chessbtn-green': cc[36][2] }"
                        v-on:click="ClickCell36()">
                        <div class="flex justify-center items-center">{{ cm[36] }}</div>
                    </td>
                    <!-- Row 4  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[37][0], 'chessbtn-blue': cc[37][1], 'chessbtn-green': cc[37][2] }"
                        v-on:click="ClickCell37()">
                        <div class="flex justify-center items-center">{{ cm[37] }}</div>
                    </td>
                    <!-- Row 4  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[38][0], 'chessbtn-blue': cc[38][1], 'chessbtn-green': cc[38][2] }"
                        v-on:click="ClickCell38()">
                        <div class="flex justify-center items-center">{{ cm[38] }}</div>
                    </td>
                    <!-- Row 4  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[39][0], 'chessbtn-blue': cc[39][1], 'chessbtn-green': cc[39][2] }"
                        v-on:click="ClickCell39()">
                        <div class="flex justify-center items-center">{{ cm[39] }}</div>
                    </td>
                </tr>
                <!-- Row 5 -->
                <tr>
                    <!-- Row 5  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[40][0], 'chessbtn-blue': cc[40][1], 'chessbtn-green': cc[40][2] }"
                        v-on:click="ClickCell40()">
                        <div class="flex justify-center items-center">{{ cm[40] }}</div>
                    </td>
                    <!-- Row 5  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[41][0], 'chessbtn-blue': cc[41][1], 'chessbtn-green': cc[41][2] }"
                        v-on:click="ClickCell41()">
                        <div class="flex justify-center items-center">{{ cm[41] }}</div>
                    </td>
                    <!-- Row 5  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[42][0], 'chessbtn-blue': cc[42][1], 'chessbtn-green': cc[42][2] }"
                        v-on:click="ClickCell42()">
                        <div class="flex justify-center items-center">{{ cm[42] }}</div>
                    </td>
                    <!-- Row 5  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[43][0], 'chessbtn-blue': cc[43][1], 'chessbtn-green': cc[43][2] }"
                        v-on:click="ClickCell43()">
                        <div class="flex justify-center items-center">{{ cm[43] }}</div>
                    </td>
                    <!-- Row 5  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[44][0], 'chessbtn-blue': cc[44][1], 'chessbtn-green': cc[44][2] }"
                        v-on:click="ClickCell44()">
                        <div class="flex justify-center items-center">{{ cm[44] }}</div>
                    </td>
                    <!-- Row 5  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[45][0], 'chessbtn-blue': cc[45][1], 'chessbtn-green': cc[45][2] }"
                        v-on:click="ClickCell45()">
                        <div class="flex justify-center items-center">{{ cm[45] }}</div>
                    </td>
                    <!-- Row 5  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[46][0], 'chessbtn-blue': cc[46][1], 'chessbtn-green': cc[46][2] }"
                        v-on:click="ClickCell46()">
                        <div class="flex justify-center items-center">{{ cm[46] }}</div>
                    </td>
                    <!-- Row 5  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[47][0], 'chessbtn-blue': cc[47][1], 'chessbtn-green': cc[47][2] }"
                        v-on:click="ClickCell47()">
                        <div class="flex justify-center items-center">{{ cm[47] }}</div>
                    </td>
                </tr>
                <!-- Row 6 -->
                <tr>
                    <!-- Row 6  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[48][0], 'chessbtn-blue': cc[48][1], 'chessbtn-green': cc[48][2] }"
                        v-on:click="ClickCell48()">
                        <div class="flex justify-center items-center">{{ cm[48] }}</div>
                    </td>
                    <!-- Row 6  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[49][0], 'chessbtn-blue': cc[49][1], 'chessbtn-green': cc[49][2] }"
                        v-on:click="ClickCell49()">
                        <div class="flex justify-center items-center">{{ cm[49] }}</div>
                    </td>
                    <!-- Row 6  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[50][0], 'chessbtn-blue': cc[50][1], 'chessbtn-green': cc[50][2] }"
                        v-on:click="ClickCell50()">
                        <div class="flex justify-center items-center">{{ cm[50] }}</div>
                    </td>
                    <!-- Row 6  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[51][0], 'chessbtn-blue': cc[51][1], 'chessbtn-green': cc[51][2] }"
                        v-on:click="ClickCell51()">
                        <div class="flex justify-center items-center">{{ cm[51] }}</div>
                    </td>
                    <!-- Row 6  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[52][0], 'chessbtn-blue': cc[52][1], 'chessbtn-green': cc[52][2] }"
                        v-on:click="ClickCell52()">
                        <div class="flex justify-center items-center">{{ cm[52] }}</div>
                    </td>
                    <!-- Row 6  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[53][0], 'chessbtn-blue': cc[53][1], 'chessbtn-green': cc[53][2] }"
                        v-on:click="ClickCell53()">
                        <div class="flex justify-center items-center">{{ cm[53] }}</div>
                    </td>
                    <!-- Row 6  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[54][0], 'chessbtn-blue': cc[54][1], 'chessbtn-green': cc[54][2] }"
                        v-on:click="ClickCell54()">
                        <div class="flex justify-center items-center">{{ cm[54] }}</div>
                    </td>
                    <!-- Row 6  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[55][0], 'chessbtn-blue': cc[55][1], 'chessbtn-green': cc[55][2] }"
                        v-on:click="ClickCell55()">
                        <div class="flex justify-center items-center">{{ cm[55] }}</div>
                    </td>
                </tr>
                <!-- Row 7 -->
                <tr>
                    <!-- Row 7  Col 0-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[56][0], 'chessbtn-blue': cc[56][1], 'chessbtn-green': cc[56][2] }"
                        v-on:click="ClickCell56()">
                        <div class="flex justify-center items-center">{{ cm[56] }}</div>
                    </td>
                    <!-- Row 7  Col 1-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[57][0], 'chessbtn-blue': cc[57][1], 'chessbtn-green': cc[57][2] }"
                        v-on:click="ClickCell57()">
                        <div class="flex justify-center items-center">{{ cm[57] }}</div>
                    </td>
                    <!-- Row 7  Col 2-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[58][0], 'chessbtn-blue': cc[58][1], 'chessbtn-green': cc[58][2] }"
                        v-on:click="ClickCell58()">
                        <div class="flex justify-center items-center">{{ cm[58] }}</div>
                    </td>
                    <!-- Row 7  Col 3-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[59][0], 'chessbtn-blue': cc[59][1], 'chessbtn-green': cc[59][2] }"
                        v-on:click="ClickCell59()">
                        <div class="flex justify-center items-center">{{ cm[59] }}</div>
                    </td>
                    <!-- Row 7  Col 4-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[60][0], 'chessbtn-blue': cc[60][1], 'chessbtn-green': cc[60][2] }"
                        v-on:click="ClickCell60()">
                        <div class="flex justify-center items-center">{{ cm[60] }}</div>
                    </td>
                    <!-- Row 7  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[61][0], 'chessbtn-blue': cc[61][1], 'chessbtn-green': cc[61][2] }"
                        v-on:click="ClickCell61()">
                        <div class="flex justify-center items-center">{{ cm[61] }}</div>
                    </td>
                    <!-- Row 7  Col 5-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[62][0], 'chessbtn-blue': cc[62][1], 'chessbtn-green': cc[62][2] }"
                        v-on:click="ClickCell62()">
                        <div class="flex justify-center items-center">{{ cm[62] }}</div>
                    </td>
                    <!-- Row 7  Col 7-->
                    <td class="border w-20 h-16"
                        v-bind:class="{ 'chessbtn-red': cc[63][0], 'chessbtn-blue': cc[63][1], 'chessbtn-green': cc[63][2] }"
                        v-on:click="ClickCell63()">
                        <div class="flex justify-center items-center">{{ cm[63] }}</div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
// import { NsStore } from "../../../store/index";
// import { storeToRefs } from "pinia";

// import { CellColorDataInit } from './ChessboardComponents/CellColor';
import { CellColorDataInit } from '../ChessboardComponents/CellColor';
// import { ChessMock, NELstMock, BRP1Mock, BRP2Mock } from './ChessboardComponents/testGame';
import { ChessMock, NELstMock, BRP1Mock, BRP2Mock } from '../ChessboardComponents/testGame';
export default {
    name: "ViewLogCom",
    components: {},
    data() {
        // const store = NsStore();
        const cm = ChessMock
        const cc = CellColorDataInit
        return {
            cm, cc
        }
    },
    methods: {},
    mounted() { },
}
</script>

<style scoped></style>