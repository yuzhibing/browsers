/**
 * Created by admin on 2017/4/14.
 */

import {get} from 'utils/fetch';


export function fetchAddressList() {
	return {
		type: 'fetchAddressList',
	}
}

export function reciveAddressList(addressList) {
	return {
		type: 'reciveAddressList',
		addressList,
	}
}

export function fetchAddressListrErr(err) {
	return {
		type: 'fetchAddressListrErr',
		err,
	}
}


export function requestAddressList() {
	return dispatch => {
		dispatch(fetchAddressList());

		get(`/api/v1/monitor/address`).then(res => {
			dispatch(reciveAddressList(res.data));
		})
			.catch(err => {
				console.log(err);
				dispatch(fetchAddressListrErr(err))
			})
	}
}