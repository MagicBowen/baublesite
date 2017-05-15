<template>
    <el-dialog title="Diagnostic Issue" :visible='formVisible' :show-close = 'false'>
        <el-form ref="form" :model="form" label-width="80px">
          <el-form-item label="Issue">
            <el-input v-model="form.issue" disabled= 'true'></el-input>
          </el-form-item>
          <el-form-item label="Time">
            <el-input v-model="form.time" disabled= 'true'></el-input>
          </el-form-item>
          <el-form-item label="Road Name">
            <el-input v-model="form.roadName" disabled= 'true'></el-input>
          </el-form-item>            
          <el-form-item label="Cause">
            <el-input v-model="form.cause"></el-input>
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
    props: ['formVisible', 'form'],

    data() {
      return {

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