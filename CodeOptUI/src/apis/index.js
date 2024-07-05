import Axios from 'axios'
import router from '../router'

if (window.localStorage.getItem('token')) {
  Axios.defaults.headers.common['Authorization'] = `Bearer ` + window.localStorage.getItem('token')
}

export let instance = Axios.create({
  baseURL:  'http://127.0.0.1:10262/api'
})


export const login = ({ loginUser, loginPassword }) => {
  console.log(loginUser, loginPassword )
  return instance.post('/login2', {
    username: loginUser,
    password: loginPassword
  })
}

export const getTaskDetails = (taskId) => {
  return instance.get('/tasks/' + taskId+ '/details')
}

export const getTaskCancel = (taskId) => {
  return instance.get('/tasks/' + taskId+ '/cancel')
}

export const getUserInfo = ({jwtstring}) => {
  return instance.get('/profile', {
    'jwt': jwtstring
  
  })
}

export const getTasks = () => {
  return instance.get('/task_table')
}

export const register = ({username, email, password}) => {
    return instance.post('/register', {
        username: username,
        email: email,
        password: password
    })

}

export const getRecentSubmissions = () => {
  return instance.get('/submit_recent');
};

export const getSubmitOverview = () => {
  return instance.get('/submit_overview');
};

export const subfile = (detail) => {
  return instance.post('/submit-code', detail)

}
export const getAvailableModels = () => {
  return instance.get('/available-models');
};

export const getTaskStatus = (taskId) => {
  return instance.get(`/task-status/${taskId}`);
};

export const getreport = (taskId) => {
  return instance.get(`/view-report/${taskId}`);
};
// respone拦截器
instance.interceptors.response.use(
    response => {
      return response
    },
    error => {
      if (error.response) {
        switch (error.response.status) {
          case 401:
            router.replace({
              path: 'login',
              query: { redirect: router.currentRoute.fullPath } // 将跳转的路由path作为参数，登录成功后跳转到该路由
            })
        }
      }
      return Promise.reject(error.response)
    }
  )

  // 添加请求拦截器，在请求头中添加JWT令牌
 instance.interceptors.request.use(config => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  });