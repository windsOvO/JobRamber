<template>
    <section>
        <nav class="navbar is-info outlined" role="navigation" aria-label="main navigation">
            <div id="navbarBasicExample" class="navbar-menu">
                <div class="navbar-start">
                    <div class="navbar-item">
                        JobRambler
                    </div>
                    <div class="navbar-item">
                        筛选条件：
                    </div>
                    <!-- 城市下拉框 -->
                    <div class="navbar-item has-dropdown is-hoverable">
                          <a class="navbar-link">
                            {{cities}}
                          </a>
                          <div class="navbar-dropdown">
                            <a v-for="(item, index) in cities_list"
                               :value="item"
                               :key="index"
                               class="navbar-item">
                               <div @click="changeCities(item)">{{item}}</div>
                             </a>
                          </div>
                    </div>
                    <!-- 行业下拉框 -->
                    <div class="navbar-item has-dropdown is-hoverable">
                          <a class="navbar-link">
                            {{industries}}
                          </a>
                          <div class="navbar-dropdown">
                            <a v-for="(item, index) in industries_list"
                               :value="item"
                               :key="index"
                               class="navbar-item">
                               <div @click="changeIndustries(item)">{{item}}</div>
                             </a>
                          </div>
                    </div>
                    <!-- 工资下拉框 -->
                    <div class="navbar-item has-dropdown is-hoverable">
                          <a class="navbar-link">
                            {{salary}}
                          </a>
                          <div class="navbar-dropdown">
                            <a v-for="(item, index) in salary_list"
                               :value="item"
                               :key="index"
                               class="navbar-item">
                               <div @click="changeSalary(item)">{{item}}</div>
                             </a>
                          </div>
                    </div>
                </div>
                <div class="navbar-end">
                    <div class="navbar-item">
                        by 软件zy1801 曹浪 aka winds
                    </div>
                </div>
            </div>
        </nav>
        <section class="hero is-fullheight-with-navbar">
            <div class="hero-body">
                <!-- 输入框 -->
                <div class="container" id="search">
                    <div class="columns">
                        <div class="column">
                            <b-field>
                                <b-input v-model="keyword" placeholder="请输入职业关键词"></b-input>
                            </b-field>
                        </div>
                        <div class="column is-one-fifth"></div>    
                    </div>
                    <button :class="statusBtn" @click="getCloud">搜索</button>
                </div>
                <div class="container" id="picture">
                <!-- 图片位置 -->
                    <div class="level">
                        <div class="level-item">
                            <img :src="img_src">
                            <!-- <img src=""> -->
                        </div>
                    </div>
                </div>
                <!-- 描述-->
                <div class="title" id="description">
                    输入你的理想职业<br>
                    获取你应该掌握的职业技能词云！
                </div>
                <!-- 无搜索结果模态框-->
                <b-modal trap-focus aria-role="dialog" v-model="noResultModal" has-modal-card>
                <div class="modal-card" style="width: auto">
                    <header class="modal-card-head">
                        <p class="modal-card-title">提示</p>
                        <button
                            type="button"
                            class="delete"
                            @click="$emit('close')"/>
                    </header>
                    <section class="modal-card-body">
                        目前条件下，无搜索返回及词云结果！
                    </section>
                    <footer class="modal-card-foot">
                        <button class="button" type="button" @click="noResultModal=false">Close</button>
                    </footer>
                </div>
                </b-modal>
            </div>
        </section>
    </section>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            keyword: '',
            cities: '不限城市',
            industries: '不限行业',
            salary: '不限工资',
            cities_list: ['不限城市', '北京', '上海', '深圳', '广州', '武汉', '杭州'],
            industries_list: ['不限行业', '互联网/电商', '游戏产业', '计算机软件', 'IT服务', '电子/芯片/半导体', '通信业'],
            salary_list: ['不限工资', '10w-15w', '15w-20w', '20w-30w', '30w-50w', '50w-100w', '100w以上'],
            img_src: '',
            statusBtnOK: 'button is-info',
            statusBtnLoading: 'button is-info is-loading',
            statusBtn: 'button is-info',
            noResultModal: false
        }
    },
    methods: {
        // 改变三个筛选条件
        changeCities (item) {
          this.cities = item
        },
        changeIndustries (item) {
          this.industries = item
        },
        changeSalary (item) {
          this.salary = item
        },
        getCloud () {
            if (this.keyword === '')
                return
            // 开始加载，禁用按钮
            this.statusBtn = this.statusBtnLoading
            this.img_src = ''

            const path = 'http://localhost:5000/api/cloud/?keyword=' + this.keyword +
                            '&city=' + this.cities +
                            '&salary=' + this.salary +
                            '&industry=' + this.industries
            // console.log(path)
            axios.get(path)
            .then(response => {
                if (response.data.info === 'success')
                    this.img_src = "./static/" + response.data.prefix +"wordcloud.png" // 图片路径
                else if (response.data.info === 'none result')
                    this.noResultModal = true
                // 加载完成，还原按钮
                this.statusBtn = this.statusBtnOK
            }).catch(err => {
                console.log(err)
            })

        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#search {
    position: absolute;
    left: 150px;
    top: 350px;
    width: 500px;
    /* background-color: antiquewhite; */
}

#picture {
    position: absolute;
    left: 800px;
    top: 300px;
    /* background-color: antiquewhite; */
}

#description {
    position: absolute;
    left: 150px;
    top: 230px;
    /* background-color: antiquewhite; */
}
</style>
