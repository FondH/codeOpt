<template>
  <div>
    <p>正在退出...</p>
  </div>
</template>

<script>
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';

export default {
  name: 'Signout',
  setup() {
    const store = useStore();
    const router = useRouter();

    onMounted(() => {
      // 调用 Vuex 中的 logOut action
      store.dispatch('logOut')
        .then(() => {
          router.push('/login'); 
        })
        .catch(error => {
          console.error('Logout failed:', error);
          router.push('/login'); 
        });
    });

    return {};
  }
};
</script>
