/**
 * Created by admin on 2017/3/3.
 */
import { Router, hashHistory, browserHistory} from 'react-router';
import React from 'react';

// 按需加载
const routers = {
  path:'/',
	getComponent(nextState,callback){
		require.ensure([],require=>{
			callback(null,require('containers/main').default);    // 按需加载时，require不能使用变量，且之前不能使用import将组件引入。如果你的组件是使用es5的module.exports导出的话，那么只需要require('components/Index')即可。而如果你的组件是使用es6的export default导出的话，那么需要加上default
		},'');
	},
  indexRoute:{
	  getComponent(nextState,callback){
		  require.ensure([],require=>{
			  callback(null,require('containers/home').default);
		  },'home');
	  },
  },
  childRoutes:[
    {
      path:'home',
	    getComponent(nextState,callback){
		    require.ensure([],require=>{
			    callback(null,require('containers/home').default);
		    },'home');
	    },
    },
    {
      path:'management',
	    getComponent(nextState,callback){
		    require.ensure([],require=>{
			    callback(null,require('containers/management').default);
		    },'management');
	    },
    }
  ]
};

export default <Router routes={routers} history={hashHistory}/>
// export default <Router routes={routers} history={browserHistory}/>    // 使用browserHistory, 当用户直接请求页面的某个子路由会报404的错误