
import {get} from 'utils/fetch';


export function fetchTransList() {
	return {
		type: 'fetchTransList',
	}
}

export function reciveTransList(transList) {
	return {
		type: 'reciveTransList',
		transList,
	}
}

export function fetchTransListrErr(err) {
	return {
		type: 'fetchTransListrErr',
		err,
	}
}


export function requestTransList(period = 'hour') {
	return dispatch => {
		dispatch(fetchTransList());

		get(`/api/v1/monitor/transaction?f=${period}`).then(res => {
			dispatch(reciveTransList(res.data));
		})
			.catch(err => {
				console.log(err);
				dispatch(fetchTransListrErr(err))
			})
	}
}