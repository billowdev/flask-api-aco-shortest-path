import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import { BestPathArrayType, CoordinatesType, NavigationArrayType, NavigationPayload } from "../../types/navigation.types";
import { RootState } from "../store";
import { NavigationType } from '../../types/navigation.types';
import * as navigationService from "../../services/navigationService"

type NavigationState = {
	// best_path: BestPathArrayType
	// coordinates: CoordinatesType
	// distance: number
	// from_start: string
	// navigation: NavigationArrayType
	// to_goal: string
	payload: any
	loading: boolean
};

const initialValues: NavigationState = {
	// best_path: [],
	// coordinates: [],
	// distance: 0,
	// from_start: "",
	// navigation: [],
	// to_goal: "",
	payload: {},
	loading: false,
};

export const getNavigation = createAsyncThunk(
	"navigation/getNavigation",
	async (data: any) => {
		return await navigationService.getNavigation(data);
	}
	// async (start: string, goal: string) => {
	// 	return await navigationService.getNavigation(start, goal);
	// }
);

const navigationSlice = createSlice({
	name: "navigation",
	initialState: initialValues,
	reducers: {
		// test_reducer: (state: NavigationState, action: PayloadAction<void>) => {
		// 	state.counter = state.counter + 1;
		// },
	},
	extraReducers: (builder) => {
		builder.addCase(getNavigation.fulfilled, (state, action) => {
			state.payload = action.payload;
			state.loading = false;
		  });
		  
		  builder.addCase(getNavigation.rejected, (state, action) => {
			state.payload = {};
			state.loading = false;
		  });
	},
});

// export const { test_reducer } = navigationSlice.actions;
export const navigationSelector = (store: RootState) => store.navigationReducer;
export default navigationSlice.reducer;
