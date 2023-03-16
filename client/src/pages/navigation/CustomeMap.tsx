import { LatLng, LatLngExpression } from 'leaflet';
import { useEffect, useState } from 'react';
import { getNavigation, navigationSelector } from "../../store/slices/navigationSlice";
import { useSelector } from "react-redux";
import { MapContainer, TileLayer, Marker, Polyline, Popup, } from 'react-leaflet';
import { useAppDispatch } from '../../store/store';

type NavigationArrayType = {
	bid: string;
	lat: string;
	lng: string;
	is_node: boolean,
}[];
// const CustomNavigationMap = ({ currentPosition }: { currentPosition: number[] }) => {
const CustomNavigationMap = () => {
	const dispatch: any = useAppDispatch();
	const navigationList: any = useSelector(navigationSelector);

	useEffect(() => {
		dispatch(getNavigation({ start: "G1", goal: "C1" }));
	}, [dispatch]);

	const [currentPosition, setCurrentPosition] = useState<[number, number]>([17.189578289590823, 104.090411954494540]); // initialize with dummy values
	// This function is called when the component mounts, and it gets the current location from the browser
	// useEffect(() => {
	// 	navigator.geolocation.getCurrentPosition(
	// 		position => setCurrentPosition([position.coords.latitude, position.coords.longitude]),
	// 		error => console.log(error)
	// 	);
	// }, []);
	const coordinates = [
		[
			17.19256404202556,
			104.09360793646384
		],
		[
			17.192329942043273,
			104.09348628794305
		],
		[
			17.192205160723507,
			104.0934495591739
		],
		[
			17.192176813324867,
			104.09343275456074
		],
		[
			17.192072053813625,
			104.09337336194189
		],
		[
			17.19192139730717,
			104.09328822535443
		],
		[
			17.191832217638694,
			104.09323194173122
		],
		[
			17.191804576414082,
			104.09321766475055
		],
		[
			17.19176518357731,
			104.0931851890825
		],
		[
			17.19182136195997,
			104.09317758265912
		],
		[
			17.191702311854886,
			104.09315242756986
		],
		[
			17.191600890270553,
			104.09309293181127
		],
		[
			17.191487969075066,
			104.09302472514737
		],
		[
			17.191392722051607,
			104.09297122443695
		],
		[
			17.19138678546207,
			104.09296904400135
		],
		[
			17.191303362818008,
			104.0929208376387
		],
		[
			17.191226020458423,
			104.09287381374162
		],
		[
			17.191193350140953,
			104.09285436772541
		],
		[
			17.191093743178683,
			104.09279492022006
		],
		[
			17.19102026439513,
			104.09275263166732
		],
		[
			17.19095823188803,
			104.0927150539265
		],
		[
			17.19091247881427,
			104.0926907907248
		],
		[
			17.189473194769665,
			104.09184172745555
		],
		[
			17.189321349733078,
			104.09192932971659
		],
		[
			17.18940353583393,
			104.09178602815216
		]
	];
	useEffect(() => {

		let counter = 0;
		const intervalId = setInterval(() => {
			setCurrentPosition([coordinates[counter][0], coordinates[counter][1]]);
			counter = (counter + 1) % coordinates.length;
		}, 1000);

		return () => clearInterval(intervalId);
	}, []);


	// useEffect(() => {
	// 	setInterval(() => {
	// 		setCurrentPosition([17.189578289590823, 104.090411954494540])

	// 		setCurrentPosition([17.188738469975437, 104.091374063713420])

	// 		setCurrentPosition([17.189400286942945, 104.091741718379720])

	// 		setCurrentPosition([17.190634027635916, 104.090406832360340])
	// 	}, 1000)

	// }, [])



	const navigation: NavigationArrayType = [

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
		},
		{
			"bid": "G1L02",
			"is_node": false,
			"lat": "17.192205160723507",
			"lng": "104.093449559173900"
		},
		{
			"bid": "G1L04",
			"is_node": false,
			"lat": "17.192176813324867",
			"lng": "104.093432754560740"
		},
		{
			"bid": "G1L6",
			"is_node": false,
			"lat": "17.192072053813625",
			"lng": "104.093373361941890"
		},
		{
			"bid": "G1L8",
			"is_node": false,
			"lat": "17.191921397307170",
			"lng": "104.093288225354430"
		},
		{
			"bid": "G1E1L01",
			"is_node": false,
			"lat": "17.191832217638694",
			"lng": "104.093231941731220"
		},
		{
			"bid": "G1E1L02",
			"is_node": false,
			"lat": "17.191804576414082",
			"lng": "104.093217664750550"
		},
		{
			"bid": "G1E1L03",
			"is_node": false,
			"lat": "17.191765183577310",
			"lng": "104.093185189082500"
		},
		{
			"bid": "E1",
			"is_node": true,
			"lat": "17.191821361959970",
			"lng": "104.093177582659120"
		},
		{
			"bid": "G1E1L04",
			"is_node": false,
			"lat": "17.191702311854886",
			"lng": "104.093152427569860"
		},
		{
			"bid": "G1E1L05",
			"is_node": false,
			"lat": "17.191600890270553",
			"lng": "104.093092931811270"
		},
		{
			"bid": "G1E1L06",
			"is_node": false,
			"lat": "17.191487969075066",
			"lng": "104.093024725147370"
		},
		{
			"bid": "G1E1L08",
			"is_node": false,
			"lat": "17.191392722051607",
			"lng": "104.092971224436950"
		},
		{
			"bid": "G1E1L07",
			"is_node": false,
			"lat": "17.191386785462070",
			"lng": "104.092969044001350"
		},
		{
			"bid": "G1E1L09",
			"is_node": false,
			"lat": "17.191303362818008",
			"lng": "104.092920837638700"
		},
		{
			"bid": "G1E1L11",
			"is_node": false,
			"lat": "17.191226020458423",
			"lng": "104.092873813741620"
		},
		{
			"bid": "G1E1L10",
			"is_node": false,
			"lat": "17.191193350140953",
			"lng": "104.092854367725410"
		},
		{
			"bid": "G1E1L12",
			"is_node": false,
			"lat": "17.191093743178683",
			"lng": "104.092794920220060"
		},
		{
			"bid": "G1E1L13",
			"is_node": false,
			"lat": "17.191020264395130",
			"lng": "104.092752631667320"
		},
		{
			"bid": "G1E1L14",
			"is_node": false,
			"lat": "17.190958231888030",
			"lng": "104.092715053926500"
		},
		{
			"bid": "G1E1L15",
			"is_node": false,
			"lat": "17.190912478814270",
			"lng": "104.092690790724800"
		},
		{
			"bid": "C1L1",
			"is_node": false,
			"lat": "17.189473194769665",
			"lng": "104.091841727455550"
		},
		{
			"bid": "C1L2",
			"is_node": false,
			"lat": "17.189321349733078",
			"lng": "104.091929329716590"
		},
		{
			"bid": "C1",
			"is_node": true,
			"lat": "17.189403535833930",
			"lng": "104.091786028152160"
		}

	]
	// This function calculates the distance between two points using the Haversine formula
	const calculateDistance = (lat1: number, lon1: number, lat2: number, lon2: number) => {
		const R = 6371; // Radius of the earth in km
		const dLat = (lat2 - lat1) * Math.PI / 180; // deg2rad below
		const dLon = (lon2 - lon1) * Math.PI / 180;
		const a =
			Math.sin(dLat / 2) * Math.sin(dLat / 2) +
			Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
			Math.sin(dLon / 2) * Math.sin(dLon / 2);
		const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
		const d = R * c; // Distance in km
		return d;
	}
	// This function finds the closest point in the navigation array to the current position
	const findClosestPoint = (lat: number, lng: number) => {
		let closestPoint = navigation[0];

		let closestDistance = calculateDistance(lat, lng, parseFloat(closestPoint.lat), parseFloat(closestPoint.lng));
		for (let i = 1; i < navigation.length; i++) {
			const distance = calculateDistance(lat, lng, parseFloat(navigation[i].lat), parseFloat(navigation[i].lng));
			if (distance < closestDistance) {
				closestPoint = navigation[i];
				closestDistance = distance;
			}
		}
		return closestPoint;
	}


	// This is the starting point (it can be replaced with the current position from GPS)
	const from_start = currentPosition.length ? [currentPosition[0], currentPosition[1]] : [0, 0];

	// This is the goal (it can be any point in the navigation array)
	const goal = [navigation[navigation.length - 1].lat, navigation[navigation.length - 1].lng];

	// This is the closest point in the navigation array to the starting point
	const closestPoint = findClosestPoint(from_start[0], from_start[1]);

	// This is the path from the starting point to the goal
	const path: LatLngExpression[] = [
		new LatLng(from_start[0], from_start[1]),
		new LatLng(parseFloat(closestPoint.lat), parseFloat(closestPoint.lng)),
		new LatLng(parseFloat(goal[0]), parseFloat(goal[1]))
	];

	const _path: LatLngExpression[] = coordinates as LatLngExpression[]

	return (
		<MapContainer center={new LatLng(from_start[0], from_start[1])} zoom={20}
			style={{ height: '100vh' }}
		>
			<TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
			<h1>{from_start[0]}</h1>
			<div>
				<Marker position={new LatLng(from_start[0], from_start[1])}>
					<Popup>
						Your current location.
					</Popup>
				</Marker>
				<Marker position={new LatLng(parseFloat(goal[0]), parseFloat(goal[1]))}>
					<Popup>
						Your goal location.
					</Popup>
				</Marker>
				<Polyline
					pathOptions={{ color: 'blue' }}
					positions={path}
					dashArray='10, 10'

				/>
				<Polyline pathOptions={{ color: 'red' }} positions={_path} />
			</div>
		</MapContainer>
	);
}

export default CustomNavigationMap;