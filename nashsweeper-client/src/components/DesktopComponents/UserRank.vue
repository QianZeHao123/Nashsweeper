<template>
    <div>
        <div class="text-xl flex justify-center items-center p-2 text-red-400">Rating of Nashsweeper players</div>
    </div>
    <div class="overflow-auto h-96">
        <table class="table-fixed w-full border-collapse">
            <thead>
                <tr>
                    <th class="w-1/4 border">PlayerID</th>
                    <th class="w-1/4  border">BR find</th>
                    <th class="w-1/4  border">Total Strategies</th>
                    <th class="w-1/4  border">Time</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Player in PlayerInfo" v-bind:key="Player">
                    <td class="border">
                        <div class="flex justify-center items-center"> {{ Player.PlayerID }}</div>
                    </td>
                    <td class="border">
                        <div class="flex justify-center items-center"> {{ Player.BRfind }}</div>
                    </td>
                    <td class="border">
                        <div class="flex justify-center items-center"> {{ Player.TotalStrategies }}</div>
                    </td>
                    <td class="border">
                        <div class="flex justify-center items-center"> {{ Player.Time }}</div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div>
        <div class="text-xl flex justify-center items-center p-4 text-purple-400">Request Data from Server</div>
    </div>
    <div class="flex justify-center items-center">
        <div class="grid grid-cols-2 gap-3 h-1/4">
            <div>
                <a class="flex justify-center items-center btn btn-sm px-8" href="">Request</a>
            </div>
            <div><a class="flex justify-center items-center btn btn-sm px-8" href="">Play Again</a></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { RatingData } from './PlayerRateMockData/RatingMockData.js'
// import { KintoneRestAPIClient } from "@kintone/rest-api-client";
// 
// 

export default {
    name: "UserRank",
    components: {},
    data() {
        const rd = RatingData
        return {
            PlayerInfo: rd
        }
    },
    methods: {
        getData: function () {
            var that = this;
            axios({
                method: 'get',
                // url: '/api/GetUserData',
                url: '/nodebridge/get-records'
            })
                .then(function (response) {
                    // console.log(response.data);
                    // that.items = response.data;
                    const originalData = response.data;
                    // 
                    const transformedData = originalData.map(item => ({
                        BRfind: item.brfind.value,
                        PlayerID: item.playerid.value,
                        TotalStrategies: parseInt(item.totoalstrategies.value, 10),
                        Time: item.time.value
                    }));

                    console.log(transformedData);


                    that.PlayerInfo = transformedData;
                    // that.name = response.data.name;
                    // that.age = response.data.age;
                    // that.address = response.data.address;
                    // 
                })
                .catch(function (error) {
                    // 处理错误情况
                    // console.log(error);
                    console.log(error.message);
                    // 
                })
        },
    },
    mounted() {
        this.getData();

        // 
        // 
        // 
    },
}
</script>

<style scoped></style>