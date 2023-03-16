import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import { BestPathArrayType, CoordinatesType, NavigationArrayType, NavigationPayload } from "../../types/navigation.types";
import { RootState } from "../store";
import { NavigationType } from '../../types/navigation.types';
import * as navigationService from "../../services/navigationService"
import { NavigationModel } from "../../models/navigation.model";

type NavigationState = {
	best_path: BestPathArrayType
	coordinates: CoordinatesType
	distance: number
	from_start: string
	navigation: NavigationArrayType
	to_goal: string
	// payload: NavigationModel
	loading: boolean
};

const initialValues: NavigationState = {
	best_path: [],
	coordinates: [],
	distance: 0,
	from_start: "",
	navigation: [],
	to_goal: "",
	// payload: {
	// 	best_path: [],
	// 	coordinates: [],
	// 	distance: 0,
	// 	from_start: "",
	// 	navigation: [],
	// 	to_goal: "",
	// },
	loading: false,
};

export const getNavigation = createAsyncThunk(
	"navigation/getNavigation",
	async (data: any) => {
		const { payload: response } = await navigationService.getNavigation(data);
		return response
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
			// state.payload = action.payload;
			state.best_path = action.payload.best_path
			state.distance = action.payload.distance
			state.navigation = action.payload.navigation
			state.from_start = action.payload.from_start
			state.to_goal = action.payload.to_goal

			state.coordinates = action.payload.coordinates
			state.loading = false;
		});

		builder.addCase(getNavigation.rejected, (state, action) => {
			state.best_path = []
			state.coordinates = []
			state.distance = 0
			state.from_start = ""
			state.to_goal = ""
			// state.payload = {
			// 	best_path: [],
			// 	coordinates: [],
			// 	distance: 0,
			// 	from_start: "",
			// 	navigation: [],
			// 	to_goal: "",
			// };
			state.loading = false;
		});
	},
});

// export const { test_reducer } = navigationSlice.actions;
export const navigationSelector = (store: RootState) => store.navigationReducer;
export default navigationSlice.reducer;
