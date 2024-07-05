<template>
<div class="container-fluid py-4">

<div class="card mb-4">
    <div class="mt-1 row">
        <div class="col-11">

            <div class="card-header pb-1">
                <h4>Standard Result</h4>
            </div>

            <div class="card-body px-2 pt-0 pb-1">
                <span class="px-3 pt-2">
                    <span style="font-weight: bold; color: #4a4a4a;">file name:</span>&nbsp;
                    <span style="color: #4a4a4a;"> {{ repots_2[0].file_name }}</span>
                </span>
                <div class="table-responsive p-0">
                    <report-table :reports="repots_2" :itemsPerPage="7" />
                </div>
            </div>

        </div>
    </div>
</div>

<div class="card mb-4">
    <div class="mt-4 row">
        <div class="col-12">


            <div class="card-header pb-1">
                <h4>Syntax Result</h4>
            </div>

            <div class="card-body px-2 pt-0 pb-1">
                <span class="px-3 pt-2">
                    <span style="font-weight: bold; color: #4a4a4a;">file name:</span>&nbsp;
                    <span style="color: #4a4a4a;"> {{ reports.file_name }}</span>
                </span>
                <div class="table-responsive p-0">
                    <report-table :reports="reports" :itemsPerPage="7" />
                </div>
            </div>

        </div>
    </div>
</div>

<!-- AI Advice Section -->
<div class="card mb-4">
    <div class="mt-4 row">
    <div class="col-12">
        <div class="card-header pb-1">
        <h4>AI Advice</h4>
        </div>
        <div class="card-body px-2 pt-0 pb-1">
        <pre class="px-3 pt-2" style="background-color: #f8f9fa; border-radius: 5px; padding: 10px; font-size: 14px;">
            {{ repots_ai_advice.join('\n') }}
        </pre>
        </div>
    </div>
    </div>
</div>

<!-- AI Generated Code Section -->
<div class="card mb-4">
    <div class="mt-4 row">
    <div class="col-12">
        <div class="card-header pb-1">
        <h4>AI Generated Code</h4>
        </div>
        <div class="card-body px-2 pt-0 pb-1">
        <pre class="px-3 pt-2" style="background-color: #2d2d2d; color: #ffffff; border-radius: 5px; padding: 10px; font-size: 14px;">
            {{ repots_ai_code.join('\n') }}
        </pre>
        </div>
    </div>
    </div>
</div>

</div>

</template>

<script setup>
import { ref, onBeforeMount } from 'vue';
import ReportTable from './components/ReportTable.vue';
import {getreport} from '@/apis'
import { useRoute } from 'vue-router';
const route = useRoute();
const taskId = route.params.taskId;

// syntax
const reports = ref([
{"file_name": "__init__.py", "file_path": "G:\\A\u5927\u4e09\u4e0b\\\u8f6f\u4ef6\u5de5\u7a0b\\codeopt\\api\\__init__.py", "type": "pylint", "res": [{"line": 1, "column": 0, "content": "", "message": "Missing module docstring", "id": "missing-module-docstring", "code": "C0114"}, {"line": 9, "column": 0, "content": "def create_app():", "message": "Missing function or method docstring", "id": "missing-function-docstring", "code": "C0116"}, {"line": 10, "column": 4, "content": "app = Flask(__name__)", "message": "Redefining name 'app' from outer scope (line 33)", "id": "redefined-outer-name", "code": "W0621"}, {"line": 17, "column": 8, "content": "from models import User,Detection,ThreadTask", "message": "Unable to import 'models'", "id": "import-error", "code": "E0401"}, {"line": 17, "column": 8, "content": "from models import User,Detection,ThreadTask", "message": "Import outside toplevel (models.User, models.Detection, models.ThreadTask)", "id": "import-outside-toplevel", "code": "C0415"}, {"line": 19, "column": 8, "content": "from views.auth import auth_blueprint", "message": "Unable to import 'views.auth'", "id": "import-error", "code": "E0401"}, {"line": 19, "column": 8, "content": "from views.auth import auth_blueprint", "message": "Import outside toplevel (views.auth.auth_blueprint)", "id": "import-outside-toplevel", "code": "C0415"}, {"line": 20, "column": 8, "content": "from views.admin import admin_blueprint", "message": "Unable to import 'views.admin'", "id": "import-error", "code": "E0401"}, {"line": 20, "column": 8, "content": "from views.admin import admin_blueprint", "message": "Import outside toplevel (views.admin.admin_blueprint)", "id": "import-outside-toplevel", "code": "C0415"}, {"line": 21, "column": 8, "content": "from views.task import task_blueprint", "message": "Unable to import 'views.task'", "id": "import-error", "code": "E0401"}, {"line": 21, "column": 8, "content": "from views.task import task_blueprint", "message": "Import outside toplevel (views.task.task_blueprint)", "id": "import-outside-toplevel", "code": "C0415"}, {"line": 22, "column": 8, "content": "from views.overview import overview_blueprint", "message": "Unable to import 'views.overview'", "id": "import-error", "code": "E0401"}, {"line": 22, "column": 8, "content": "from views.overview import overview_blueprint", "message": "Import outside toplevel (views.overview.overview_blueprint)", "id": "import-outside-toplevel", "code": "C0415"}, {"line": 17, "column": 8, "content": "from models import User,Detection,ThreadTask", "message": "Unused User imported from models", "id": "unused-import", "code": "W0611"}, {"line": 17, "column": 8, "content": "from models import User,Detection,ThreadTask", "message": "Unused Detection imported from models", "id": "unused-import", "code": "W0611"}, {"line": 17, "column": 8, "content": "from models import User,Detection,ThreadTask", "message": "Unused ThreadTask imported from models", "id": "unused-import", "code": "W0611"}]}
]);
// standard
const repots_2 = ref([
{"file_name": "__init__.py", "file_path": "G:\\A\u5927\u4e09\u4e0b\\\u8f6f\u4ef6\u5de5\u7a0b\\codeopt\\api\\__init__.py", "type": "pylint", "res": [{"line": 9, "column": 1, "message": "expected 2 blank lines, found 0", "type": "checkstyle", "content": "def create_app():"}, {"line": 17, "column": 9, "message": "'models.User' imported but unused", "type": "checkstyle", "content": "from models import User,Detection,ThreadTask"}, {"line": 17, "column": 9, "message": "'models.Detection' imported but unused", "type": "checkstyle", "content": "from models import User,Detection,ThreadTask"}, {"line": 17, "column": 9, "message": "'models.ThreadTask' imported but unused", "type": "checkstyle", "content": "from models import User,Detection,ThreadTask"}, {"line": 17, "column": 32, "message": "missing whitespace after ','", "type": "checkstyle", "content": "from models import User,Detection,ThreadTask"}, {"line": 17, "column": 42, "message": "missing whitespace after ','", "type": "checkstyle", "content": "from models import User,Detection,ThreadTask"}]}
]);

const repots_ai_advice = ref(['wu']);
const repots_ai_code = ref(['wu']);


const fetchreport = async () => {
  try {
    const response = await getreport(taskId);
    if (response.status === 200) {
      let res = response.data.res;
      console.log(res);

      repots_2.value[0] = JSON.parse(res.standard_check_res);
      console.log(JSON.parse(res.standard_check_res));

      reports.value[0] = JSON.parse(res.syntax_check_res);

      console.log("123", res.ai_res);
      let aiRes;
      if (typeof res.ai_res === 'string') { // 如果 res.ai_res 是字符串
        aiRes = JSON.parse(res.ai_res);
      } else { // 如果 res.ai_res 已经是对象
        aiRes = res.ai_res;
      }
      
      if (aiRes) {
        repots_ai_advice.value[0] = aiRes.advice;
        repots_ai_code.value[0] = aiRes.code;
      }
    }
  } catch (error) {
    console.error('Error fetching task status:', error);
    // 显示错误消息而不是刷新页面
    alert('Error fetching task status. Please try again later.');
  }
};

onBeforeMount(() => {
  fetchreport().then(() => {
    console.log("Data updated:", repots_ai_advice.value[0]);
  });
});
</script>

<style scoped>
.text-sm {
  font-size: 0.875rem;
}

.align-middle {
  vertical-align: middle;
}

.text-center {
  text-align: center;
}

.text-xs {
  font-size: 0.75rem;
}

.font-weight-bold {
  font-weight: bold;
}

.mb-0 {
  margin-bottom: 0;
}

.min-height-300 {
  min-height: 300px;
}

.mask {
  display: block;
  height: 100%;
}

.bg-gradient-success {
  background: linear-gradient(87deg, #11cdef 0, #1171ef 100%) !important;
}

pre {
  white-space: pre-wrap; /* Wraps long lines to fit in the container */
  word-wrap: break-word; /* Breaks long words to fit in the container */
}
</style>