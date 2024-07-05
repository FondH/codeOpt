<script>
import { ref } from 'vue';
import TaskTable from "./components/TaskTable.vue";
export default {
  components:{
    TaskTable
  },
  setup() {
    const selectedTaskDetails = ref(null);
    const isSelected = ref(false);

    const handleTaskDetails = ({ details, isSelected: selected }) => {
      selectedTaskDetails.value = details;
      isSelected.value = selected;
    };

    const closeDetails = () => {
      isSelected.value = false;
      selectedTaskDetails.value = null;
    };

    return {
      selectedTaskDetails,
      isSelected,
      handleTaskDetails,
      closeDetails,
    };
  },
};
</script>
<template>
  <div class="py-4 container-fluid">
    <div class="mt-4 row">
      <div class="col-12">
        <TaskTable @task-details="handleTaskDetails" />
      </div>
    </div>


    <div class="mt-4 row">
       <!-- Task Details -->
      <h6>Task Details</h6>
      {{selectedTaskDetails}}
      <div v-if="selectedTaskDetails && isSelected" class="card mt-4">
        <div class="card-header pb-0 d-flex justify-content-between" style="position: relative;">
          <button class="btn btn-link text-danger mb-2 " @click="closeDetails" style="position: absolute; top: 0; right: 0;">
            <i class="fa fa-times" aria-hidden="true"></i>
          </button>
        </div>
        <div class="card-body px-0 pt-0 pb-2">
          <div class="table-responsive p-0">
            <table class="table align-items-center mb-0">
              <thead>
                <tr>
                  <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">Key</th>
                  <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">Value</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="text-xs font-weight-bold mb-0">Task ID</td>
                  <td class="text-xs">{{ selectedTaskDetails.task_id }}</td>
                </tr>
                <tr>
                  <td class="text-xs font-weight-bold mb-0">Detection ID</td>
                  <td class="text-xs">{{ selectedTaskDetails.detection_id }}</td>
                </tr>
                <tr>
                  <td class="text-xs font-weight-bold mb-0">Progress</td>
                  <td class="text-xs">{{ selectedTaskDetails.progress }}%</td>
                </tr>
                <tr>
                  <td class="text-xs font-weight-bold mb-0">Status</td>
                  <td class="text-xs">{{ selectedTaskDetails.status }}</td>
                </tr>
                <tr>
                  <td class="text-xs font-weight-bold mb-0">Submit Time</td>
                  <td class="text-xs">{{ selectedTaskDetails.submit_time }}</td>
                </tr>
                <tr>
                  <td class="text-xs font-weight-bold mb-0">File Name</td>
                  <td class="text-xs">{{ selectedTaskDetails.file_name }}</td>
                </tr>
                <tr>
                  <td class="text-xs font-weight-bold mb-0">Use Large Model</td>
                  <td class="text-xs">{{ selectedTaskDetails.use_large_model }}</td>
                </tr>
                <tr>
                  <td class="text-xs font-weight-bold mb-0">Model</td>
                  <td class="text-xs">{{ selectedTaskDetails.model }}</td>
                </tr>
                <tr>
                  <td class="text-xs font-weight-bold mb-0">Prompt</td>
                  <td class="text-xs">{{ selectedTaskDetails.prompt }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>


</template>
