/**
 * Created by admin on 2017/4/14.
 */

 import axios from 'axios';

const baseURL = 'http://47.98.52.13:5000/';
const headers = {
	'Content-Type': 'application/json',
	'Access-Control-Allow-Methods': 'GET, POST, PUT',
	'Access-Control-Allow-Origin': '*',
	'Access-Control-Allow-Headers': 'X-Requested-With'
};

const http = axios.create({
  // baseURL,
  // timeout: 1000,
  // headers
});



export const get = function (url, params) {
	// let URL = baseUrl + url;
	// console.log('URL:', URL)
	// return Promise.resolve(function () {
		return http.get(url, {params})
	// }())
};

export const post = (url, params) => {
	// return Promise.resolve(function () {
		return http.post(url, params)
	// }())
};