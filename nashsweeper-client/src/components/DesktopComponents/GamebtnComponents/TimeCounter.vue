<!-- this component achieve the time counter in PartB -->
<!-- While touch this button for the first time, it will begin countering the time -->
<!-- While touch this button for the other time, it will stop countering -->
<template>
    <div class="w-full h-full">
        <div class="btn h-full w-full border rounded-md bg-yellow-500" v-on:click="onClickTimeCounter()">
            Time counter: {{ time.hour }}:{{ time.minute }}:{{ time.second }}
        </div>
    </div>
</template>

<script>
// import startHandler from './startHandler'
import { NsStore } from '../../../store/index.js'
import { storeToRefs } from 'pinia'
export default {
    name: "TimeCounter",
    comphournts: {},
    data() {
        const store = NsStore()
        const { time } = storeToRefs(store)

        // const second = store.time.second
        return {
            // hour: '00',
            // hour,
            // minute,
            // second,
            time,
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
        onClickTimeCounter() {
            if (this.buttonValue == 0) {
                this.flag = setInterval(() => {
                    if (this.time.second === 59 || this.time.second === '59') {
                        this.time.second = '00';
                        this.second_counter = 0;
                        if (this.time.minute === 59 || this.time.minute === '59') {
                            this.time.minute = '00';
                            this.minute_counter = 0;
                            if (this.hour_counter + 1 <= 9) {
                                this.hour_counter++;
                                this.time.hour = '0' + this.hour_counter;
                            } else {
                                this.hour_counter++;
                                this.time.hour = this.hour_counter;
                            }
                        } else {
                            if (this.minute_counter + 1 <= 9) {
                                this.minute_counter++;
                                this.time.minute = '0' + this.minute_counter;
                            } else {
                                this.minute_counter++;
                                this.time.minute = this.minute_counter;
                            }
                        }
                    } else {
                        if (this.second_counter + 1 <= 9) {
                            this.second_counter++;
                            this.time.second = '0' + this.second_counter;
                        } else {
                            this.second_counter++;
                            this.time.second = this.second_counter;
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
    mounted() {
        this.onClickTimeCounter()
    },
}
</script>

<style scoped></style>