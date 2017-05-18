<template>
  <div>
    <el-row>
      <el-col :span="24"><div class="grid-content bg-purple-dark" style="height:100px;"></div></el-col>
    </el-row>
    <el-row :gutter="5">
      <el-col :span="4">
            <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose" theme="dark" router="true" style="height:400px;">
              <el-menu-item index="home">List</el-menu-item>
              <el-menu-item index="chart">Chart</el-menu-item>
            </el-menu>
      </el-col>
      <el-col :span="20">
        <router-view></router-view>
      </el-col>
    </el-row>
  </div>
</template>

<style>
  #bauble {
    margin-top: 50px;
  }
  .el-row {
    margin-bottom: 5px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>