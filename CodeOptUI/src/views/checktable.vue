<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { subfile } from '@/apis';
import { useStore } from "vuex";
const router = useRouter();
const store = useStore();
// State variables
const file = ref(null);
const fileInput = ref(null);
const githubRepo = ref('');
const uploadMethod = ref('file');
const codeLanguage = ref('');
const detectStrength = ref('medium');
const detectModules = ref([]);
const useLargeModel = ref(false);
const modelOptions = ref({
  model: '',
  prompt: ''
});
const availableModels = ref([]);
const isLoading = ref(false);
const submitterName = ref('');
const submitTime = ref(new Date().toLocaleString());

// Sample prompts for reference
const samplePrompts = [
  "To complete a software engineering assignment",
  "For a research project",
  "To improve code quality"
];

// Fetch available models from server on mount
onMounted(async () => {
  try {
    const response = await axios.get('/api/available-models');
    availableModels.value = response.data.models;
  } catch (error) {
    console.error('Error fetching models:', error);
  }
});

const handleFileChange = () => {
  if (fileInput.value) {
    file.value = fileInput.value.files[0];
  }
};

const submitCode = async () => {
  isLoading.value = true;
  const formData = new FormData();
  formData.append('user_id', store.state.userInfo.user_id); // file or github
  formData.append('uploadMethod', uploadMethod.value); // file or github
  if (uploadMethod.value === 'file' && file.value) {
    formData.append('file', file.value);
    formData.append('fileName', file.value.name);
    formData.append('fileSize', file.value.size);
  } else {
    formData.append('githubRepo', githubRepo.value);
  }
  formData.append('submitterName', submitterName.value);
  formData.append('submitTime', submitTime.value);
  formData.append('codeLanguage', codeLanguage.value);
  formData.append('detectStrength', detectStrength.value);
  formData.append('detectModules', JSON.stringify(detectModules.value));
  formData.append('useLargeModel', useLargeModel.value);
  if (useLargeModel.value) {
    formData.append('model', modelOptions.value.model);
    formData.append('prompt', modelOptions.value.prompt);
  }

  // 打印 FormData 的键值对
//   for (const pair of formData.entries()) {
//     console.log(`${pair[0]}: ${pair[1]}`);
//   }
console.log(file.value)
  try {
    const response = await subfile(formData);
    const taskId = response.data.task_id;
    router.push(`/task-status/${taskId}`);
  } catch (error) {
    console.error('Error submitting code:', error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="container-fluid">
    <h2>Submit Code for Review</h2>
    <form @submit.prevent="submitCode">
      <div class="mb-3">
        <label for="submitterName" class="form-label">Submitter Name</label>
        <input type="text" id="submitterName" class="form-control" v-model="submitterName" required />
      </div>
      <div class="mb-3">
        <label for="uploadMethod" class="form-label">Select Upload Method</label>
        <select id="uploadMethod" class="form-control" v-model="uploadMethod">
          <option value="file">Upload from Local File System</option>
          <option value="github">Enter GitHub Repository URL</option>
        </select>
      </div>
      <div v-if="uploadMethod === 'file'" class="mb-3">
        <label for="file" class="form-label">Upload Code File</label>
        <input type="file" id="file" class="form-control" @change="handleFileChange" ref="fileInput" />
      </div>
      <div v-if="uploadMethod === 'github'" class="mb-3">
        <label for="githubRepo" class="form-label">GitHub Repository URL</label>
        <input type="text" id="githubRepo" class="form-control" v-model="githubRepo" />
      </div>
      <div class="mb-3">
        <label for="codeLanguage" class="form-label">Code Language</label>
        <select id="codeLanguage" class="form-control" v-model="codeLanguage" required>
          <option value="C++">C++</option>
          <option value="C">C</option>
          <option value="Java">Java</option>
          <option value="Python">Python</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="detectStrength" class="form-label">Detection Strength</label>
        <select id="detectStrength" class="form-control" v-model="detectStrength">
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="detectModules" class="form-label">Detection Modules</label>
        <div class="form-check">
          <input type="checkbox" id="module1" class="form-check-input" value="codeStyle" v-model="detectModules" />
          <label for="module1" class="form-check-label">Code Style Detection</label>
        </div>
        <div class="form-check">
          <input type="checkbox" id="module2" class="form-check-input" value="syntaxAnalysis" v-model="detectModules" />
          <label for="module2" class="form-check-label">Code Syntax Analysis</label>
        </div>
        <div class="form-check">
          <input type="checkbox" id="module3" class="form-check-input" value="vulnerabilityDetection" v-model="detectModules" />
          <label for="module3" class="form-check-label">Code Vulnerability Detection</label>
        </div>
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" id="useLargeModel" class="form-check-input" v-model="useLargeModel" />
        <label for="useLargeModel" class="form-check-label">Use Large Model</label>
      </div>
      <div v-if="useLargeModel" class="mb-3">
        <label for="model" class="form-label">Model</label>
        <select id="model" class="form-control" v-model="modelOptions.model">
          <option v-for="model in availableModels" :key="model" :value="model">{{ model }}</option>
        </select>
        <label for="prompt" class="form-label mt-2">Prompt</label>
        <input type="text" id="prompt" class="form-control" v-model="modelOptions.prompt" />
        <small class="form-text text-muted">Sample Prompts:</small>
        <ul>
          <li v-for="prompt in samplePrompts" :key="prompt">{{ prompt }}</li>
        </ul>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    <div v-if="isLoading" class="mt-4">
      <h3>Processing...</h3>
      <!-- 可以在这里添加一个加载动画 -->
    </div>
  </div>
</template>
