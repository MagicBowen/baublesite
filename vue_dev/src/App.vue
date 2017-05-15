<template>
  <div id="app">
    <img src="./assets/logo.png">
      <el-table
        :data="diagnostics"
        highlight-current-row
        border
        stripe
        fit>
        <el-table-column
          prop="time"
          label="Time">
        </el-table-column>  
        <el-table-column
          prop="issue"
          label="Issue">
        </el-table-column>
        <el-table-column
          prop="roadName"
          label="Road">
        </el-table-column>
        <el-table-column
          prop="cause"
          label="Cause">
        </el-table-column>
        <el-table-column
          prop="comment"
          label="Comment">
        </el-table-column>
        <el-table-column>
          <template scope="scope">
            <el-button type="text" size="small" @click='onEdit(scope.$index)'>edit</el-button>
          </template>
        </el-table-column>        
      </el-table>
      <add-form :form-visible='addNewVisible' @onSubmit= 'onAddNew' @onCancel= 'onAddCancel'></add-form>
      <edit-form :form-visible='editVisible' :form= 'editIssue' @onSubmit= 'onEditDone' @onCancel= 'onEditCancel'></edit-form>
      <el-button @click='handleAddNew'>add new</el-button>
  </div>
</template>

<script>

import queryAll from './influx.js'
import addNew from './AddNew.vue'
import editForm from './EditForm.vue'

export default {
  data () {
    return {
      diagnostics: [],
      addNewVisible: false,
      editVisible: false,
      editIssue: {issue:'', date:'', time:'', comment:''}
    }
  },

  components: {
    'add-form' : addNew,
    'edit-form' : editForm
  },

  mounted: function () {
    var vm = this;
    queryAll().then(result => {
      vm.diagnostics = result;
      for(var i = 0; i < vm.diagnostics.length; i++)
      {
        vm.diagnostics[i].time = vm.diagnostics[i].time.toString();
      }
      alert(`type = ${typeof(vm.diagnostics[0].time)}, value = ${vm.diagnostics.time}`);
    });
  },

  methods: {
    handleAddNew(){
      this.$data.addNewVisible = true;
    },
    onAddNew(){
      alert('add new');
      this.$data.addNewVisible = false;
    },
    onAddCancel(){
      this.$data.addNewVisible = false;
    },
    onEditDone(){
      this.$data.editVisible = false;
    },
    onEditCancel(){
      this.$data.editVisible = false;
    },
    onEdit(index){
      this.editIssue = this.diagnostics[index];
      this.$data.editVisible = true;
    }
  }
}
</script>

<style>
body {
  font-family: Helvetica, sans-serif;
}
</style>
