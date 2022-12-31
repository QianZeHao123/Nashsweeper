<!-- this component achieve the time counter in PartB -->
<!-- While touch this button for the first time, it will begin countering the time -->
<!-- While touch this button for the other time, it will stop countering -->
<template>
    <div>
        <!-- <div class="border rounded-md p-2 bg-yellow-300" @click="startHandler()"> -->
        <div class="border rounded-md p-2" @click="onClickTimeCounter()">
            Time counter: {{ hour }}:{{ minute }}:{{ second }}
        </div>
        <!-- </div> -->
    </div>
</template>

<script>
// import startHandler from './startHandler'
export default {
    name: "TimeCounter",
    comphournts: {},
    data() {
        return {
            hour: '00',
            minute: '00',
            second: '00',
            flag: null,
            second_counter: 0, // 秒的计数
            minute_counter: 0, // 分的计数
            hour_counter: 0, // 时的计数
            buttonValue: 0,
        }
    },
    props: {
        msg: String
    },
    methods: {
        // 开始计时
        // startHandler() {
        //     this.flag = setInterval(() => {
        //         if (this.second === 60 || this.second === '60') {
        //             this.second = '00';
        //             this.second_counter = 0;
        //             if (this.minute === 60 || this.minute === '60') {
        //                 this.minute = '00';
        //                 this.minute_counter = 0;
        //                 if (this.hour_counter + 1 <= 9) {
        //                     this.hour_counter++;
        //                     this.hour = '0' + this.hour_counter;
        //                 } else {
        //                     this.hour_counter++;
        //                     this.hour = this.hour_counter;
        //                 }
        //             } else {
        //                 if (this.minute_counter + 1 <= 9) {
        //                     this.minute_counter++;
        //                     this.minute = '0' + this.minute_counter;
        //                 } else {
        //                     this.minute_counter++;
        //                     this.minute = this.minute_counter;
        //                 }
        //             }
        //         } else {
        //             if (this.second_counter + 1 <= 9) {
        //                 this.second_counter++;
        //                 this.second = '0' + this.second_counter;
        //             } else {
        //                 this.second_counter++;
        //                 this.second = this.second_counter;
        //             }
        //         }

        //     }, 100)
        // },
        // 暂停计时
        // endHandler() {
        //     this.flag = clearInterval(this.flag)
        // },
        onClickTimeCounter() {
            if (this.buttonValue == 0) {
                this.flag = setInterval(() => {
                    if (this.second === 60 || this.second === '60') {
                        this.second = '00';
                        this.second_counter = 0;
                        if (this.minute === 60 || this.minute === '60') {
                            this.minute = '00';
                            this.minute_counter = 0;
                            if (this.hour_counter + 1 <= 9) {
                                this.hour_counter++;
                                this.hour = '0' + this.hour_counter;
                            } else {
                                this.hour_counter++;
                                this.hour = this.hour_counter;
                            }
                        } else {
                            if (this.minute_counter + 1 <= 9) {
                                this.minute_counter++;
                                this.minute = '0' + this.minute_counter;
                            } else {
                                this.minute_counter++;
                                this.minute = this.minute_counter;
                            }
                        }
                    } else {
                        if (this.second_counter + 1 <= 9) {
                            this.second_counter++;
                            this.second = '0' + this.second_counter;
                        } else {
                            this.second_counter++;
                            this.second = this.second_counter;
                        }
                    }

                }, 1000)
                this.buttonValue = 1;
            }
            else {
                this.flag = clearInterval(this.flag)
                this.buttonValue = 0;
            }
        },
    },
    mounted() { },
}
</script>

<style scoped>

</style>