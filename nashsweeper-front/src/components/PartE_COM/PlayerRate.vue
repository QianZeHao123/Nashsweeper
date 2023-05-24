<template>
    <div>
        <div class="text-xl flex justify-center items-center p-2 text-red-400">Rating of Nashsweeper players</div>
    </div>
    <div class="overflow-auto h-96">
        <table class="table-fixed w-full border-collapse">
            <thead>
                <tr>
                    <th class="w-1/4 border">Index</th>
                    <th class="w-1/4  border">Player ID</th>
                    <th class="w-1/4  border">Total strategies</th>
                    <th class="w-1/4  border">Time(s)</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="Player in PlayerInfo" v-bind:key="Player">
                    <td class="border">
                        <div class="flex justify-center items-center"> {{ Player.index }}</div>
                    </td>
                    <td class="border">
                        <div class="flex justify-center items-center"> {{ Player.PlayerID }}</div>
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
                <a class="flex justify-center items-center btn btn-sm px-8" href="http://198.74.121.61:803">Request</a>
            </div>
            <div><button class="flex justify-center items-center btn btn-sm px-8">Play Again</button></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
// if fail linking to the backend server, show the Mock data
import { RatingData } from './PlayerRateMockData/RatingMockData.js'
export default {
    name: "PlayerRate",
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
                url: '/GetUserData/test'
            })
                .then(function (response) {
                    // 处理成功情况
                    console.log(response.data);
                    // that.items = response.data;
                    that.PlayerInfo = response.data;
                    // that.name = response.data.name;
                    // that.age = response.data.age;
                    // that.address = response.data.address;

                })
                .catch(function (error) {
                    // 处理错误情况
                    // console.log(error);
                    console.log(error.message);
                    
                })
        },
    },
    mounted() {
        this.getData();
    },
}
</script>

<style scoped></style>