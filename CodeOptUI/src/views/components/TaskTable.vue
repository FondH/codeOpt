

<script>
import { defineComponent } from 'vue';
import { ref, onMounted } from 'vue';
import { getTasks, getTaskDetails, getTaskCancel} from '@/apis';

export default defineComponent({
  setup(props, { emit }) {
    const tasks = ref([]);
    const selectedTaskDetails = ref(null);
    const isSelected = ref(false);
    window.tasks = tasks;
    window.selectedTaskDetails = selectedTaskDetails;

    const fetchTasks = async () => {
      try {
        const response = await getTasks();
        tasks.value = response.data.results;
      } catch (error) {
        console.error('Error fetching tasks:', error);
      }
    };

    const cancelTask = async (taskId) => {
      try {
        await getTaskCancel(taskId);
        fetchTasks();
      } catch (error) {
        console.error('Error cancelling task:', error);
      }
    };

    const fetchTaskDetails = async (taskId) => {
      try {
        console.log("<fetchTaskDetails>: taskId(" + taskId)
        const response = await getTaskDetails(taskId);
        selectedTaskDetails.value = response.data;
        isSelected.value = true;
        emit('task-details', { details: selectedTaskDetails.value, isSelected: isSelected.value });
       } catch (error) {
        console.error('Error fetching task details:', error);
      }
    };
  
    const viewResults = () => {
      // 跳转到结果页或打开模态框显示结果
    };
    const closeDetails = () => {
      isSelected.value = false;
      selectedTaskDetails.value = null;
    };
    onMounted(fetchTasks);

    return {
      tasks,
      cancelTask,
      fetchTaskDetails,
      viewResults,
      closeDetails,
    };
  },
});
</script>

<template>
  <div class="card mb-4">
    <div class="card-header pb-0">
      <h6>Tasks table</h6>
    </div>
    <div class="card-body px-0 pt-0 pb-2">
      <div class="table-responsive p-0">
        <table class="table align-items-center justify-content-center mb-0">
          <thead>
            <tr>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7">
                Submitter
              </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                Time
              </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder opacity-7 ps-2">
                Status
              </th>
              <th class="text-uppercase text-secondary text-xxs font-weight-bolder text-center opacity-7 ps-2">
                Completion
              </th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="task in tasks" :key="task.id">
              <td>
                <div class="d-flex px-2">
                  <div class="my-auto">
                    <h6 class="mb-0 text-sm">{{ this.$store.state.userInfo.username }}</h6>
                  </div>
                </div>
              </td>
              <td>
                <p class="text-sm font-weight-bold mb-0">{{ task.submit_time }}</p>
              </td>
              <td>
                <span class="text-xs font-weight-bold">{{ task.status }}</span>
              </td>
              <td class="align-middle text-center">
                <div class="d-flex align-items-center justify-content-center">
                  <span class="me-2 text-xs font-weight-bold">{{ task.progress  }}%</span>
                  <div>
                    <div class="progress">
                      <div
                        class="progress-bar"
                        :class="{
                          'bg-gradient-info': task.status === 'working' || task.status === 'pending',
                          'bg-gradient-success': task.status === 'done',
                          'bg-gradient-danger': task.status === 'canceled'
                        }"
                        role="progressbar"
                        :aria-valuenow="task.completion"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        :style="{ width: task.progress  + '%' }"
                      ></div>
                    </div>
                  </div>
                </div>
              </td>
              <td class="align-middle">
                <div class="dropdown">
                  <button
                    class="btn btn-link text-secondary mb-0"
                    type="button"
                    id="dropdownMenuButton"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    <i class="fa fa-ellipsis-v text-xs" aria-hidden="true"></i>
                  </button>
                  <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <li v-if="task.status === 'working' || 'pending'">
                      <a class="dropdown-item" href="#" @click="cancelTask(task.task_id)">Cancel</a>
                    </li>
                    <li v-if="task.status === 'working'|| 'pending'">
                      <a class="dropdown-item" href="#" @click="fetchTaskDetails(task.task_id)">View Details</a>
                    </li>
                    <li v-if="task.status === 'done'">
                      <a class="dropdown-item" href="#" @click="viewResults(task.task_id)">View Results</a>
                    </li>
                  </ul>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

    <!-- Task Details -->

</template>

