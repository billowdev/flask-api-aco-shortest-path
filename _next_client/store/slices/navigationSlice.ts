import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "../store";
import * as navigationService from "@/services/navigationService"
import { BestPathArrayType, CoordinatesType, NavigationArrayType } from "@/models/navigation.model";
import { NavigationModel } from './../../models/navigation.model';

type NavigationState = {
	best_path: BestPathArrayType
	coordinates: CoordinatesType
	distance: number
	from_start: string
	navigation: NavigationArrayType
	to_goal: string
	// payload: NavigationModel
	loading: boolean,
	navigations: NavigationModel
};

const initialValues: NavigationState = {
	best_path: ["G1",
			"G1L01",],
			coordinates: [[
				17.19256404202556,
				104.09360793646384
			],
			[
				17.192329942043273,
				104.09348628794305
			],],
	distance: 1.3155167600975681,
	from_start: "G1",
	navigation: [
		{
			"bid": "G1",
			"is_node": true,
			"lat": "17.192564042025560",
			"lng": "104.093607936463840"
		},
		{
			"bid": "G1L01",
			"is_node": false,
			"lat": "17.192329942043273",
			"lng": "104.093486287943050"
		}
	],
	to_goal: "G1L01",
	navigations: {
		best_path: ["G1",
			"G1L01",],
		coordinates: [[
			17.19256404202556,
			104.09360793646384
		],
		[
			17.192329942043273,
			104.09348628794305
		],],
		distance: 1.3155167600975681,
		from_start: "G1",
		navigation: [
			{
				"bid": "G1",
				"is_node": true,
				"lat": "17.192564042025560",
				"lng": "104.093607936463840"
			},
			{
				"bid": "G1L01",
				"is_node": false,
				"lat": "17.192329942043273",
				"lng": "104.093486287943050"
			}
		],
		to_goal: "G1L1",
	},
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
			state.navigations = action.payload;
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
			state.loading = false;
		});
	},
});

// export const { test_reducer } = navigationSlice.actions;
// export const navigationSelector = (store: RootState) => store.navigationReducer;


export const navigationSelector = (store: RootState): NavigationModel | undefined => store.navigation.navigations;



export default navigationSlice.reducer;

