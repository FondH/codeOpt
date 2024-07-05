import {register,login, getUserInfo } from '@/apis'

export default {
    toggleSidebarColor({ commit }, payload) {
        commit("sidebarType", payload);
    },

    toLogin ({ commit }, info) {
        console.log("Actions : toLogin, parameters of info:", info)

        return new Promise((resolve, reject) => {
            login(info).then(res => {
                if (res.status === 200) {
                    console.log(res.data)
                    commit('LOGIN', res.data.access_token)
                    commit('SET_AUTH', true)
                    let userInfo = {
                        username:res.data.username,
                        user_id:res.data.user_id,
                        rank:res.data.rank
                    }
                    commit('SET_USER', userInfo)
                    window.localStorage.setItem('token', res.data.access_token)
                    window.localStorage.setItem('userInfo', JSON.stringify(userInfo));
                    window.localStorage.setItem('isAuthenticated', true);
                    
                    resolve(res)
                }
            }).catch((error) => {
                console.log(error)
                reject(error)
            })
        })
    },
    toRegister({ commit },info){
        return new Promise((resolve,reject) => {
            console.log("Actions : toRegister, parameters of info:", info)
            register(info).then(res => {
                if(res.status === 200){
                    console.log(res.data)
                    commit('SET_AUTH', false)
                    resolve(res)
                }
            }).catch((error) => {
                console.log(error)
                reject(error)
            })
        })
    },
    getUser ({ commit }) {
        return new Promise((resolve, reject) => {
            getUserInfo().then(res => {
            if (res.status === 200) {
                commit('SET_PROFILE', {})
                resolve(res)
            }
            }).catch((error) => {
            reject(error)
            })
        })
    },
    logOut ({ commit }) {
        console.log("Actions : logOut")
        return new Promise(() => {
            commit('SET_USER', null)
            commit('SET_AUTH', false)
            commit('SET_PROFILE', {})
            commit('LOGIN', '')
            window.localStorage.removeItem('token')
        })
    },

    updateModelSettings({ commit }, newSettings) {
        commit('setModelSettings', newSettings);
        window.localStorage.setItem('modelSettings', JSON.stringify(newSettings));
    },

    updateAlgorithmSettings({ commit }, newSettings) {
        commit('setAlgorithmSettings', newSettings);
        window.localStorage.setItem('algorithmSettings', JSON.stringify(newSettings));
    }
  
}