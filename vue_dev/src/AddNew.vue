<template>
    <el-dialog title="Diagnostic Issue" :visible='formVisible' :show-close = 'false' style="background-color:#1F2D3D;">
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="Issue">
            <el-input v-model="form.issue"></el-input>
          </el-form-item>
          </el-form-item>
          <el-form-item label="Time">
            <el-col :span="11">
              <el-date-picker type="date" placeholder="选择日期" v-model="form.date" style="width: 100%;"></el-date-picker>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
              <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.time" style="width: 100%;"></el-time-picker>
            </el-col>
          </el-form-item>
          <el-form-item label="Comment">
            <el-input type="textarea" v-model="form.comment"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit">submit</el-button>
            <el-button @click='onCancel'>cancel</el-button>
          </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
  export default {
    props: ['formVisible'],

    data() {
      return {
        form: {issue : '',
               date: '',
               time: '',
               comment: ''
        }
      };
    },

    methods: {
      onSubmit() {
        this.$emit('onSubmit');
      },
      onCancel() {
        this.$emit('onCancel');
      }
    }    
  };
</script>
<style>
  html {
    font-size: 12px;
    font-family: Ubuntu, simHei, sans-serif;
    font-weight: 400
  }

  body {
    font-size: 1rem
  }    
</style>