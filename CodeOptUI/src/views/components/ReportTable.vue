<!-- ReportTable.vue -->
<script setup>
import { ref, computed } from 'vue';
import ArgonPagination from '@/components/ArgonPagination.vue';
import ArgonPaginationItem from '@/components/ArgonPaginationItem.vue';

const props = defineProps({
  reports: {
    type: Array,
    required: true,
  },
  itemsPerPage: {
    type: Number,
    default: 10,
  },
});

const currentPage = ref(1);

const flattenedReports = computed(() => {
  return props.reports.flatMap(report => 
    report.res.map(res => ({
      file_name: report.file_name,
      ...res
    }))
  );
});

const paginatedReports = computed(() => {
  const start = (currentPage.value - 1) * props.itemsPerPage;
  const end = currentPage.value * props.itemsPerPage;
  return flattenedReports.value.slice(start, end);
});

const totalPages = computed(() => {
  return Math.ceil(flattenedReports.value.length / props.itemsPerPage);
});

const setCurrentPage = (page) => {
  currentPage.value = page;
};

const highlightContent = (content, column) => {
  if (!content || column === undefined) return content || '';
  const before = content.slice(0, column);
  const highlighted = content.slice(column, column + 1);
  const after = content.slice(column + 1);
  return `${before}<span class="highlighted">${highlighted}</span>${after}`;
};
</script>

<template>
  <div>
    <div class="pb-0 card-header mb-0">
 </div>
    <table class="table align-items-center justify-content-center mb-0">
      <thead>
        <tr>
          <th>Type</th>
          <th>Code</th>
          <th>Line</th>
          <th>Message</th>
          <th>Severity</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(report, index) in paginatedReports" :key="index">
          <td>{{ report.id || '' }}</td>
          <td v-html="highlightContent(report.content, report.column)"></td>
          <td>{{ report.line || '' }}</td>
          <td class="message">{{ report.message || '' }}</td>
          <td>{{ report.severity || '' }}</td>
        </tr>
      </tbody>
    </table>

    <argon-pagination :color="'primary'" :size="'md'">
      <argon-pagination-item
        v-for="page in totalPages"
        :key="page"
        :label="page"
        :active="page === currentPage.value"
        @click="setCurrentPage(page)"
      />
    </argon-pagination>
  </div>
</template>

<style>
.table {
  width: 100%;
  border-collapse: collapse;
  border: 1px solid #333; /* 改为更明显的颜色 */
}

.table th,
.table td {
  border: 1px solid #333; /* 改为更明显的颜色 */
  padding: 8px;
}

.table th {
  background-color: #f2f2f2;
  text-align: left;
}

.message {
  white-space: pre-wrap;
  word-break: break-word; /* 确保自动换行 */
}

table tr:nth-child(even) {
  background-color: #f2f2f2;
}

.highlighted {
  background-color: yellow;
  color: red;
  font-weight: bold;
  border: 1px solid red;
  padding: 0 2px;
}
</style>
