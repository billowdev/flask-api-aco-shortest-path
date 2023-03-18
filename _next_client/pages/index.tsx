import { getNavigation, navigationSelector } from "@/store/slices/navigationSlice";
import { useAppDispatch } from "@/store/store";
import React from "react";
import { useSelector } from "react-redux";
import dynamic from "next/dynamic";
type Props = {};
const ShowMap = dynamic(() => import("./navigation/show"), { ssr: false });
const Index = ({}: Props) => {

  // const dispatch: any = useAppDispatch();
	// const navigationList: any = useSelector(navigationSelector);

	// React.useEffect(() => {
	// 	dispatch(getNavigation({ start: "G1", goal: "C1" }));
	// }, [dispatch]);

  
  return (
    <>
      <ShowMap />
    </>
  );
};

export default Index;
