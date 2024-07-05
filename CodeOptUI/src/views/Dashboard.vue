<script setup>
import MiniStatisticsCard from "@/examples/Cards/MiniStatisticsCard.vue";
import GradientLineChart from "@/examples/Charts/GradientLineChart.vue";
import Carousel from "./components/Carousel.vue";
// import CategoriesList from "./components/CategoriesList.vue";
import { ref, onBeforeMount } from 'vue';
import { getSubmitOverview,getRecentSubmissions } from '@/apis';


const chartKey = ref(0); // 用于强制重新挂载组件的key
const description = ref('<i class=\'fa fa-arrow-up text-success\'></i><span class=\'font-weight-bold\'>0</span> 提交记录');
const chartData = ref({
    labels: [ 
    'Apr', 'May','Jun', 'Jul',  'Aug', 'Sep',  'Oct',  'Nov', 'Dec'
    ],
 
   datasets: [
    {
      label: 'submit times',
      data: [50, 40, 300, 220, 500, 250, 400, 230, 500],
    },
  ],

});

// Generate default data if API request fails for <LineChart>
const generateDefaultData = () => {
  const labels = [];
  const data = [];
  const today = new Date();
  for (let i = 7; i >= 0; i--) {
    const date = new Date(today);
    date.setDate(today.getDate() - i);
    labels.push(date.toISOString().split('T')[0]); // 格式化日期为 YYYY-MM-DD
    labels.push(i+'')
    data.push(0); // 默认记录数为0
  }
  chartData.value.labels = labels;
  chartData.value.datasets[0].data = data;
  console.log(chartData.value)
};

const fetchSubmitOverview = async () => {
  try {

    const response = await getSubmitOverview();
    const data = response.data;
    description.value = `<i class='fa fa-arrow-up text-success'></i>
    <span class='font-weight-bold'>${data.total_submissions}</span> records`;

    chartData.value.labels = data.labels;
    chartData.value.datasets[0].data = data.data;
    chartKey.value++; // 更新key以强制重新挂载组件

  } catch (error) {
    chartKey.value++; // 更新key以强制重新挂载组件
    console.error('Error fetching submit overview, using default data:', error);
    generateDefaultData();
  }
};

const submissions = ref([]);
// get data for <table>
const fetchRecentSubmissions = async () => {
  try {
    const response = await getRecentSubmissions();
    
    submissions.value = response.data.submissions;
    //         'task_id':task.task_id,
            // 'submitter': det.submitter_name,
            // 'fileName': det.file_name,
            // 'submitTime': det.submit_time,
            // 'status': submission.status
  } catch (error) {
    console.error('Error fetching recent submissions:', error);
  }
};


onBeforeMount(() => { 
  console.log(chartData.value)
  fetchSubmitOverview();  
  fetchRecentSubmissions();
});


</script>
<template>
  <div class="py-4 container-fluid">
    <div class="row">
      <div class="col-lg-12">
        <div class="row">
          <div class="col-lg-3 col-md-6 col-12">
            <mini-statistics-card
              title="check"
              value=""
              description="submit a piece of code"
              :icon="{
                component: 'fas fa-check-circle',
                background: 'bg-gradient-primary',
                shape: 'rounded-circle',
              }"
              @click="() => $router.push('/check')"
              style="cursor: pointer;"
            />
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <mini-statistics-card
              title="tasks"
              value=""
              description="surf your records"
              :icon="{
                component: 'fas fa-table',
                background: 'bg-gradient-danger',
                shape: 'rounded-circle',
              }"
              @click="() => $router.push('/tables')"
              style="cursor: pointer;"
            />
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <mini-statistics-card
              title="team"
              value=""
              description="share works with team"
              :icon="{
                component: 'fas fa-users',
                background: 'bg-gradient-success',
                shape: 'rounded-circle',
              }"
              @click="() => $router.push('/teams')"
              style="cursor: pointer;"
            />
          </div>
          <div class="col-lg-3 col-md-6 col-12">
            <mini-statistics-card
              title="progrom"
              value=""
              description="deploy our progrom"
              :icon="{
                component: 'fab fa-github',
                background: 'bg-gradient-warning',
                shape: 'rounded-circle',
              }"
              @click="() => window.open('https://github.com/your-repo', '_blank')"
              style="cursor: pointer;"
            />
          </div>
        </div>

        <div class="row">
          <div class="col-lg-7 mb-lg">

              <!-- line chart -->
              <div class="card z-index-2">
                <gradient-line-chart
                  :key="chartKey" 
                  id="chart-line"
                  title="submition overview"
                  :description="description"
                  :chart="chartData"
                />
              </div>


            
            
            <!-- <div class="card z-index-2">
              <gradient-line-chart
                id="chart-line"
                title="Sales Overview"
                description="<i class='fa fa-arrow-up text-success'></i>
      <span class='font-weight-bold'>4% more</span> in 2021"
                :chart="{
                  labels: [
                    'Apr',
                    'May',
                    'Jun',
                    'Jul',
                    'Aug',
                    'Sep',
                    'Oct',
                    'Nov',
                    'Dec',
                  ],
                  datasets: [
                    {
                      label: 'Mobile Apps',
                      data: [50, 40, 300, 220, 500, 250, 400, 230, 500],
                    },
                  ],
                }"
              />
            </div> -->

          </div>
     
          
          <div class="col-lg-5">
            <carousel />
          </div>

        </div>
        <div class="row mt-4">
          
    <div class="col-lg-7 mb-lg-0 mb-4">
    <div class="card">
      <div class="p-3 pb-0 card-header">
        <div class="d-flex justify-content-between">
          <h6 class="mb-2">latest records</h6>
        </div>
      </div>
      <div class="table-responsive">
        <table class="table align-items-center">
          <thead>
            <tr>
              <th>detection</th>
              <th>file name</th>
              <th>time</th>
              <th>status</th>
              <th> report</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(submission, index) in submissions" :key="index">
              <td class="w-30">
                <div class="px-2 py-1 d-flex align-items-center">
                  <div class="ms-4">
                    <p class="mb-0 text-xs font-weight-bold">
                        {{ submission.submitter }}
                    </p>
                    <h6 class="mb-0 text-sm"></h6>
                  </div>
                </div>
              </td>
              <td>
                <div class="text-center">
                  <p class="mb-0 text-xs font-weight-bold">{{ submission.fileName }}</p>
                  <h6 class="mb-0 text-sm"></h6>
                </div>
              </td>
              <td>
                <div class="text-center">
                  <p class="mb-0 text-xs font-weight-bold">{{ submission.submitTime }}</p>
                  <h6 class="mb-0 text-sm"></h6>
                </div>
              </td>
              <td class="text-sm align-middle">
                <div class="text-center col">
                  <p class="mb-0 text-xs font-weight-bold">{{ submission.status }}</p>
                  <h6 class="mb-0 text-sm"></h6>
                </div>
              </td>

              <td class="text-sm align-middle">
                <div class="text-center col">
                  <p class="mb-0 text-xs font-weight-bold">
           
                    <router-link :to="`/report/${submission.task_id}`">
                    
                      <i class="ni ni-bold-right">view</i>
                    </router-link>
                  </p>
                  <h6 class="mb-0 text-sm"></h6>
                </div>
              </td>

            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
          <!-- <div class="col-lg-5">
            <categories-list
              :categories="[
                {
                  icon: {
                    component: 'ni ni-mobile-button',
                    background: 'dark',
                  },
                  label: 'Devices',
                  description: '250 in stock <strong>346+ sold</strong>',
                },
                {
                  icon: {
                    component: 'ni ni-tag',
                    background: 'dark',
                  },
                  label: 'Tickets',
                  description: '123 closed <strong>15 open</strong>',
                },
                {
                  icon: { component: 'ni ni-box-2', background: 'dark' },
                  label: 'Error logs',
                  description: '1 is active <strong>40 closed</strong>',
                },
                {
                  icon: { component: 'ni ni-satisfied', background: 'dark' },
                  label: 'Happy Users',
                  description: '+ 430',
                },
              ]"
            />
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>
