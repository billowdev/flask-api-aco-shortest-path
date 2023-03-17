import { useState } from "react";
import NavigationMap from "@/components/NavigationMap";
import * as navigationService from "@/services/navigationService"

export default function MyPage() {
	const [payload, setPayload] = useState({
		best_path: [],
		coordinates: [],
		distance: 0,
		from_start: "",
		navigation: [],
		to_goal: "",
	});

	// Assume that you have some logic to fetch the payload data from the backend
	// and update the state accordingly.
	// For the sake of simplicity, let's assume that you have a button that fetches
	// the data and updates the state when clicked.
	const handleFetchData = async () => {
		const response = await navigationService.getNavigation({ start: "G1", goal: "A9" });
		console.log('====================================');
		console.log(response.payload);
		console.log('====================================');
		setPayload(response.payload);
	};

	return (
		<div>
			<h1>Navigation Map</h1>
			<button onClick={handleFetchData}>Fetch Data</button>
			{payload.best_path.length > 0 && (
				<NavigationMap
					bestPath={payload.best_path}
					coordinates={payload.coordinates} navigation={payload.navigation} />
			)}
		</div>
	);
}
