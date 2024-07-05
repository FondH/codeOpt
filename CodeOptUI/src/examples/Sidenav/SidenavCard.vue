<script setup>
import { computed } from "vue";
import { useStore } from "vuex";
const store = useStore();

const isRTL = computed(() => store.state.isRTL);
const layout = computed(() => store.state.layout);
defineProps({
  card: {
    type: Object,
    required: true,
    title: String,
    description: String,
    links: {
      type: Array,
      label: String,
      route: String,
      color: String,
    },
  },
});
</script>
<template>
  <div
    v-show="layout !== 'landing'"
    class="card card-plain shadow-none"
    id="sidenavCard"
  >
    <div class="p-3 card-body text-center w-100 pt-0">
      <img
        class="w-50 mx-auto"
        src="@/assets/img/illustrations/icon-documentation.svg"
        alt="sidebar_illustration"
      />

      <h6 v-if="isRTL" class="mb-0 text-dark up">任何需求</h6>

      <h6 v-else class="mb-0 text-dark up">Need Help ?</h6>

      <p v-if="isRTL" class="text-xs font-weight-bold">
       请参见doc文档进一步查看      </p>

      <p v-else class="text-xs font-weight-bold">Please check our docs</p>
    </div>

    <a
      v-if="isRTL"
      href="https://www.creative-tim.com/learning-lab/vue/overview/argon-dashboard/"
      target="_blank"
      class="mb-3 btn btn-dark btn-sm w-100"
    >
      helper 在这里
    </a>

    <a
      v-else
      href="https://www.creative-tim.com/learning-lab/vue/overview/argon-dashboard/"
      target="_blank"
      class="mb-3 btn btn-dark btn-sm w-100"
    >
      Documentation
    </a>

    <a
      v-if="isRTL"
      href="https://www.creative-tim.com/product/vue-argon-dashboard-pro"
      target="_blank"
      class="mb-3 btn btn-success btn-sm w-100"
    >
      仓库链接在这里
    </a>

    <a
      v-else
      href="https://www.creative-tim.com/product/vue-argon-dashboard-pro"
      target="_blank"
      class="mb-3 btn btn-success btn-sm w-100"
    >
      Github
    </a>
  </div>
</template>
