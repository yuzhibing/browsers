/**
 * Created by admin on 2017/4/14.
 */

import {get} from 'utils/fetch';


export function fetchPriceTrend() {
	return {
		type: 'fetchPriceTrend',
	}
}

export function recivePriceTrend(list) {
	return {
		type: 'recivePriceTrend',
		list,
	}
}

export function fetchPriceTrendErr(err) {
	return {
		type: 'fetchPriceTrendErr',
		err,
	}
}


export function requestPriceTrend(period) {
	return dispatch => {
		dispatch(fetchPriceTrend());

		get(`/api/v1/monitor/price?period=${period}`).then(res => {
			dispatch(recivePriceTrend(res.data));
		})
			.catch(err => {
				console.log(err);
				dispatch(fetchPriceTrendErr(err))
			})
	}
}