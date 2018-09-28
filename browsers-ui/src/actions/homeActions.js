/**
 * Created by admin on 2017/4/14.
 */

import {get} from 'utils/fetch';


export function fetchHomeOrder() {
	return {
		type: 'fetchHomeOrder',
	}
}

export function reciveHomeOrder(orders) {
	return {
		type: 'reciveHomeOrder',
		orders,
	}
}

export function fetchHomeOrderErr(err) {
	return {
		type: 'fetchHomeOrderErr',
		err,
	}
}


export function requestHomeOrder() {
	return dispatch => {
		dispatch(fetchHomeOrder());

		get(`/api/v1/monitor/order`).then(res => {
			dispatch(reciveHomeOrder(res.data));
		})
			.catch(err => {
				console.log(err);
				dispatch(fetchHomeOrderErr(err))
			})
	}
}