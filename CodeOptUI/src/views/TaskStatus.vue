<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const taskId = route.params.taskId;
const taskStatus = ref('Pending');
const taskDetails = ref({});
const reportLink = ref('');
;
const fetchTaskStatus = async () => {
  try {
    const response = await axios.get(`/api/task-status/${taskId}`);
    taskStatus.value = response.data.status;
    taskDetails.value = response.data.details;
    if (response.data.report_link) {
      reportLink.value = response.data.report_link;
    }
  } catch (error) {
    console.error('Error fetching task status:', error);
  }
};

onMounted(() => {
  fetchTaskStatus();
  setInterval(fetchTaskStatus, 5000); // 每5秒查询一次任务状态
});
</script>

<template>

  <div class="py-4 container-fluid">
    <div class="row col-12">
 
      <div class="card">

        <div class="card-header pb-0" >
          <h4>Task id: {{ taskId }}</h4>
        </div>
        <div class="card-body  pt-0 pb-2" >
          <div v-if="taskStatus === 'Pending'">
            <h4>Waiting for the task to start...</h4>
          </div>
          <div v-else-if="taskStatus === 'In Progress'">
            <h3>Task is in progress. Please wait...</h3>
            <p>Processing: {{ taskDetails.progress }}%</p>
          </div>
          <div v-else-if="taskStatus === 'Completed'">
            <h3>Task completed!</h3>
            <a :href="reportLink" target="_blank">Download Report</a>
          </div>
          <div v-else>
            <h3>Unknown status: {{ taskStatus }}</h3>
          </div>
        </div>
      </div>
    </div>


    <div class="mt-4 row">
      <div class="col-12">

           <div class="card mt-4">
      <div class="card-header pb-0">
        <h6>Task Details</h6>
      </div>
      <div class="card-body px-0 pt-0 pb-2">
        <div class="table-responsive p-0">
          <table class="table align-items-center mb-0">
            <thead>
              <tr>
                <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Field</th>
                <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">Details</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="text-xs font-weight-bold">Submitter</td>
                <td class="text-xs">{{ taskDetails.submitterName }}</td>
              </tr>
              <tr>
                <td class="text-xs font-weight-bold">Submission Time</td>
                <td class="text-xs">{{ taskDetails.submitTime }}</td>
              </tr>
              <tr v-if="taskDetails.uploadMethod === 'file'">
                <td class="text-xs font-weight-bold">File Name</td>
                <td class="text-xs">{{ taskDetails.fileName }}</td>
              </tr>
              <tr v-if="taskDetails.uploadMethod === 'file'">
                <td class="text-xs font-weight-bold">File Size</td>
                <td class="text-xs">{{ taskDetails.fileSize }} bytes</td>
              </tr>
              <tr v-if="taskDetails.uploadMethod === 'github'">
                <td class="text-xs font-weight-bold">GitHub Repository</td>
                <td class="text-xs">{{ taskDetails.githubRepo }}</td>
              </tr>
              <tr>
                <td class="text-xs font-weight-bold">Code Language</td>
                <td class="text-xs">{{ taskDetails.codeLanguage }}</td>
              </tr>
              <tr>
                <td class="text-xs font-weight-bold">Detection Strength</td>
                <td class="text-xs">{{ taskDetails.detectStrength }}</td>
              </tr>
              <tr>
                <td class="text-xs font-weight-bold">Detection Modules</td>
                <td class="text-xs">{{ taskDetails.detectModules }}</td>
              </tr>
              <tr v-if="taskDetails.useLargeModel">
                <td class="text-xs font-weight-bold">Model</td>
                <td class="text-xs">{{ taskDetails.model }}</td>
              </tr>
              <tr v-if="taskDetails.useLargeModel">
                <td class="text-xs font-weight-bold">Prompt</td>
                <td class="text-xs">{{ taskDetails.prompt }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
      </div>
    </div>
  </div>



  
   


</template>
