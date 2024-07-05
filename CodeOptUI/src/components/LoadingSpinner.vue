<template>
  <div class="loading-spinner">
    <div class="spinner"></div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.loading-spinner {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 6px solid #f3f3f3;
  border-top: 6px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
